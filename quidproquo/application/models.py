from application import db
from flask_wtf import Flaskform
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.widgets import PasswordInput
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.column(db.String(15))
    password = db.Column(db.String(15), nullable=False)
    property = db.Column(db.Integer)
    cash = db.Column(db.Integer)
    investments = db.Column(db.Integer)

class Loans(db.Model):
    loan_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount_borrowed = db.Column(db.Integer)
    amount_paid = db.column(db.Integer)
    lender_id = db.Column(db.String(20))

