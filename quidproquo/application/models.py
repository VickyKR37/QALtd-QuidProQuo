from application import db, app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.widgets import PasswordInput
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

class Users(db.Model):
    user_name = db.Column(db.String(15), primary_key=True)
    user_id = db.relationship('user_id', backref='userbr')
    password = db.Column(db.String(15), nullable=False)
    property = db.Column(db.Integer)
    cash = db.Column(db.Integer)
    investments = db.Column(db.Integer)

    def __repr__(self):
        return 'Choose {}'.format(self.user_name)

class Loans(db.Model):
    loan_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount_borrowed = db.Column(db.Integer)
    amount_paid = db.column(db.Integer)
    lender_id = db.Column(db.String(20))

    def __repr__(self):
        return 'Choose {}'.format(self.lender_id)

class AddProfile(FlaskForm):
    user_name = StringField('Username')
    password = StringField('Password')
    property = IntegerField('Value of Property')
    cash = IntegerField('Value of Cash')
    investments = IntegerField('Value of Investmensts')
    sumbit = SubmitField('Create Your Profile')

class AddDebtDetails(FlaskForm):
    lender_id = SelectField('Lenders Name', choices=[
        ('barclays', 'Barclays'), 
        ('co-operative_bank', 'Co-operative Bank'), 
        ('halifax', 'Halifax'), 
        ('hsbc', 'HSBC'), 
        ('lloyds', 'Lloyds'), 
        ('metro', 'Metro'), 
        ('natwest', 'Natwest')])
    amount_borrowed = IntegerField('Amount Borrowed')
    amount_paid = IntegerField('Amount Paid Back')
    submit = SubmitField('Add the details of your debt')




