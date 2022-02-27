from flask_wtf import FlaskForm
from wtforms.validators import data_required, email_validator
from wtforms import StringField,SubmitField, EmailField, IntegerField, DateField, TextAreaField,SelectField,SelectFieldBase, PasswordField
from wtforms_sqlalchemy.fields import QuerySelectField


class Login(FlaskForm):
	user_name = StringField(label='Username', validators=[data_required()])
	password = PasswordField('Password', validators=[data_required()])
	submit = SubmitField()

class CheckOut(FlaskForm):
	pass


class Register(FlaskForm):
	name = StringField(label='First Name', validators=[data_required()])
	last_name = StringField(label='Last Name', validators=[data_required()])
	country = StringField(label='Country', validators=[data_required()])
	city = StringField(label='City', validators=[data_required()])
	street = StringField(label='Street', validators=[data_required()])
	house_number = IntegerField(label='House Number', validators=[data_required()])
	phone_num = IntegerField(label='Phone Number')
	email = EmailField(label='Email', validators=[data_required(message='Come on man enter your email!!')])
	password = PasswordField('Password', validators=[data_required()])
	username = StringField(label='User Name', validators=[data_required()])
	submit = SubmitField()

class Addons(FlaskForm):
	pass