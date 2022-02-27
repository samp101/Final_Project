from app import db
import datetime
from flask_login import UserMixin
#
#
# availability_in_country = db.Table('film_country',
#                       db.Column('film_id', db.Integer, db.ForeignKey('film.film_id')),
#                       db.Column('country_id', db.Integer, db.ForeignKey('country.country_id'))
# )
#
# films_category_table = db.Table('film_category',
#                       db.Column('film_id', db.Integer, db.ForeignKey('film.film_id')),
#                       db.Column('category_id', db.Integer, db.ForeignKey('category.category_id'))
# )
#
# directors_table  = db.Table('director_film',
#                       db.Column('film_id', db.Integer, db.ForeignKey('film.film_id')),
#                       db.Column('director_id', db.Integer, db.ForeignKey('director.director_id'))
# )
#
#
# class Country(db.Model):
#     country_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     films = db.relationship('Film', backref='country',lazy='dynamic')
#     available_film = db.relationship('Film', secondary=availability_in_country, back_populates='available_in_countries')
#
#
# class Category(db.Model):
#     category_id = db.Column(db.Integer, primary_key=True)
#     category = db.Column(db.String())
#
#     films = db.relationship('Film', secondary=films_category_table,back_populates="categories")
#
#
# class Film(db.Model):
#
#     film_id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String())
#     release_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
#     country_id = db.Column(db.Integer, db.ForeignKey('country.country_id'))
#
#     available_in_countries = db.relationship('Country', secondary=availability_in_country,back_populates="available_film")
#     categories = db.relationship('Category', secondary=films_category_table,back_populates="films")
#     director = db.relationship('Director', secondary=directors_table,back_populates="film",uselist=False )
#
# class Director(db.Model):
#     director_id = db.Column(db.Integer, primary_key=True)
#     director_name = db.Column(db.String())
#     director_lastName = db.Column(db.String())
#     film = db.relationship('Film', secondary=directors_table,back_populates="director")
#
#
#
#
#
#
# dogs_table = db.Table('dogs',
#                       db.Column('human_id', db.Integer, db.ForeignKey('human.id')),
#                       db.Column('dog_id', db.Integer, db.ForeignKey('dog.id'))
# )
#
# class Human(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     dogs = db.relationship("Dog", secondary=dogs_table)
#
# class Dog(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


# class Food(db.Model):
#     pass




class User(UserMixin,db.Model):


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique = True)
    password = db.Column(db.String())
    name = db.Column(db.String())
    last_name = db.Column(db.String())
    country = db.Column(db.String())
    city = db.Column(db.String())
    street = db.Column(db.String())
    house_number = db.Column(db.Integer())
    phone_num = db.Column(db.Integer(), unique=True)
    email = db.Column(db.String(), unique=True)

    def get_reset_password_token(self, expires_in=600):
        timeout = time.time() + expires_in
        payload = {
            'reset_password': self.id,
            'exp': timeout
        }

        # Get the secret key from config
        secret_key = app.config['SECRET_KEY']

        # Create the token
        token = jwt.encode(payload)

        # Turn it to string
        s_token = token.decode('utf-8')

        return s_token

    def verify_reset_password_token(self, token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    # def cart(self, food, dict):
    #     self.food = food
    #     self.dict = dict
    #     self.dict = {}
    #     self.dict[] = []
    #     return self.dict['cart'].append(self.food)









class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    img_link = db.Column(db.String())
    price = db.Column(db.Integer)
    selected = db.Column(db.Boolean(), default = False)

class Condiments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    img_link = db.Column(db.String())
    selected = db.Column(db.Boolean(), default = False)

class Sides(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    img_link = db.Column(db.String())
    price = db.Column(db.Integer)
    selected = db.Column(db.Boolean(), default = False)

class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    img_link = db.Column(db.String())
    price = db.Column(db.Integer)
    selected = db.Column(db.Boolean(), default = False)

class Veggies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    img_link = db.Column(db.String())
    selected = db.Column(db.Boolean(), default = False)

class Bread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    img_link = db.Column(db.String())
    selected = db.Column(db.Boolean(), default = False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    price = price = db.Column(db.Integer)
    add_ons = db.Column(db.String())

class Purchase_history(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String())
    food_name = db.Column(db.String())
    total = db.Column(db.Integer)



#
# a = Veggies(name='Pickles',img_link='pickles.png')
# c = Veggies(name='Peppers',img_link='peppers.png')
# b = Veggies(name='Tomatos',img_link='tomato.png')
#
# e = Condiments(name='Ketchup',img_link='ketchup.png')
# d = Veggies(name='Lettuce',img_link='lettuce.png')
# f = Condiments(name='Hot Sauce',img_link='hot-sauce.png')
# g = Condiments(name='Mustard', img_link='mustard.png')
# #
# e = Bread(name='Whole Wheat',img_link='ww.png')
# f = Bread(name='White Bread',img_link='wb.png')
#
# i = Food(name='Double Burger',img_link='double-burger.png', price=24.99)
# h = Food(name='Single Burger',img_link='single-burger.png', price=18.99)
# j = Food(name='Hot Dog',img_link='hot-dog.png', price=15.99)
# special = Food(name='Burger Special',img_link='special.png', price=29.99)

w = Sides(name='Wings', img_link='wings.png', price=10.99)
a = Sides(name='Salad', img_link='salad.png', price=5.99)
r = Sides(name='Fries', img_link='fries.png', price=2.99)
t = Sides(name='Onion Rings', img_link='onion-rings.png', price=3.99)



#     id = db.Column(db.Integer, primary_key=True)
# class Register(db.Model):
#
#     name = db.Column(db.String())
#     last_name = db.Column(db.String())
#     country = db.Column(db.String())
#     city = db.Column(db.String())
#     street = db.Column(db.String())
#     house_number = db.Column(db.Integer())
#     phone_num = db.Column(db.Integer())
#     email = db.Column(db.String(), unique= True)
#     username = db.Column(db.String(), unique = True)
#     password = db.Column(db.String())







