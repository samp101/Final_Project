import flask
import flask_login
from flask_mail import Message
from app import app, db, login_manager, mail
from app.forms import Login,Register,CheckOut
from app.models import User,Food,Condiments,Veggies,Bread,Order,Sides

cart = []
order_temp = []
food = Food.query.all()
sides_query = Sides.query.all()
def clear_order():
    clear_order = Order.query.all()
    for delete in clear_order:
        db.session.delete(delete)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods = ['GET','POST'])
@app.route('/homepage', methods = ['GET','POST'])
def login():
    if flask_login.current_user.is_authenticated:  # Check if the user is not already logged in
        return flask.redirect(flask.url_for('menu'))

    form = Login()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.user_name.data).first()

        if user is None or not user.password == form.password.data:
            form.user_name.data = form.user_name.data
            flask.flash('Invalid username or password')

            return flask.redirect(flask.url_for('login'))

        flask_login.login_user(user, remember=True)
        return flask.redirect(flask.url_for('menu'))

    return flask.render_template('homepage.html',form=form)

@app.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()

    clear_order = Order.query.all()
    for delete in clear_order:
        db.session.delete(delete)
    db.session.commit()

    return flask.redirect(flask.url_for('login'))

@app.route('/register', methods = ['GET','POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        user = User(name=form.name.data, last_name=form.last_name.data, city=form.city.data,
                    country=form.country.data, street=form.street.data, house_number=form.house_number.data,
                    phone_num=form.phone_num.data, email=form.email.data, username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return flask.redirect(flask.url_for('login'))

    return flask.render_template('register-div-page-copy.html',form = form)

@app.route('/selected_condiments/<id>/<selected_food>')
@flask_login.login_required
def selected(id,selected_food):

    if id in order_temp:
        order_temp.remove(id)
    else:
        order_temp.append(id)


    return flask.redirect(flask.url_for('selected_food',selected_food=selected_food))

@app.route('/selected_condiment/<id>/<selected_food>')
@flask_login.login_required
def selecte(id,selected_food):

    if id in order_temp:
        order_temp.remove(id)
    else:
        order_temp.append(id)


    return flask.redirect(flask.url_for('selected_sides',selected_food=selected_food))



@app.route('/menu')
@flask_login.login_required
def menu():
    flask.session['cart'] = cart
    return flask.render_template('menu.html',user=flask_login.current_user,food = food,cart=cart,)

@app.route('/sides')
@flask_login.login_required
def sides():

    flask.session['cart'] = cart
    return flask.render_template('sides.html',user=flask_login.current_user,sides= sides_query, cart=cart,)
@app.route('/food/<selected_food>')
@flask_login.login_required
def selected_food(selected_food):
    condiments1 = Condiments.query.all()
    veggies = Veggies.query.all()
    bread = Bread.query.all()

    return flask.render_template('selected-food.html',user=flask_login.current_user,cart=cart,food = food, selected_food = selected_food, condiments = condiments1, veggies=veggies,breads=bread,order=order_temp)

@app.route('/sides/<selected_food>')
@flask_login.login_required
def selected_sides(selected_food):
    condiments1 = Condiments.query.all()
    veggies = Veggies.query.all()
    bread = Bread.query.all()

    return flask.render_template('selected-sides.html',user=flask_login.current_user,cart=cart, sides= sides_query, selected_food = selected_food, condiments = condiments1, veggies=veggies,breads=bread,order=order_temp)

@app.route('/add-to-cart/<food_name>/<price>')
@flask_login.login_required
def add_to_cart(food_name,price):
    condimen = " ".join(order_temp)
    order = Order(name = food_name, price = price, add_ons = condimen )
    db.session.add(order)
    db.session.commit()
    order_temp.clear()
    flask.flash(f'Your {food_name} was added succesfully ')

    return flask.redirect(flask.url_for('menu'))


@app.route('/cart')
@flask_login.login_required
def cart_basket():
    total = 0
    order_checkout = Order.query.all()
    for a in order_checkout:
        total += a.price
    return flask.render_template('cart.html', food=food,  user=flask_login.current_user,order=order_checkout,total = total)

@app.route('/delete/<id>')
@flask_login.login_required
def delete_product(id):
    delete_prod  = Order.query.get(id)
    db.session.delete(delete_prod)
    db.session.commit()
    return flask.redirect(flask.url_for('cart_basket'))




@app.route('/send_mail/<id>')
@flask_login.login_required
def send_mail(id):
    tc=0

    ordered = Order.query.all()
    for a in ordered:
        cart.append(a.name)
        tc += a.price

    food_order = ' ,'.join(cart)

    msg = Message('Order', recipients = [id]  )
    msg.html = f'Hello '+ flask_login.current_user.name + ' here is you order. '+ food_order + 'It will cost $'+ str(tc) +' Have a great day!!'
    mail.send(msg)

    cart.clear()
    tc=0

    clear_order = Order.query.all()
    for delete in clear_order:
        db.session.delete(delete)

    db.session.commit()
    #
    # ordered = Order.query.all()
    #
    # for order in ordered:
    #     order_hist = Purchase_history(person_name = order.person_name, food_name = order.name,total=order.price)
    #     db.session.add(order_hist)
    #     db.session.commit()
    #

    flask.flash('Order has been sent! ')
    return flask.redirect(flask.url_for('menu'))
