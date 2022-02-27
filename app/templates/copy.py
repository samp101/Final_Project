<!DOCTYPE html>
<html lang="en">
<body>
<div>
    <button style=""><a href="{{ url_for('cart_basket') }}"> Cart </a></button>
    <a href="{{ url_for('menu') }}">Home</a>
    {% if current_user.is_anonymous %}
    <a href="{{ url_for('login') }}">Sign In</a>
    {% else %}
    <a href="{{ url_for('logout') }}">Logout</a>
    {% endif %}
</div>
<h2>
    Hello {{ user.username }}
    Hello {{ user.email }}

    {% with messages = get_flashed_messages() %}
  {% if messages %}
    {% for message in messages %}
      {{ message }}
    {% endfor %}
  {% endif %}
{% endwith %}




</h2>

<button style=""><a href="{{ url_for('logout') }}">Log out </a></button>
<button style=""><a href="{{ url_for('send_mail', id =user.email ) }}">Send </a></button>

{% for food in cart %}
<h1> {{ food }}  </h1>
{% endfor %}

{% for types in food %}

<div class = 'menu-food-card'>

    <a href="{{ url_for('selected_food', selected_food=types.name) }}">
        <img src="/static/images/hamburger-top-2235831.jpg", width=400px alt="{{ types.name }}">
        {{ types.name }}


    </a>
</div>
    {% endfor %}
</body>
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
</html>