from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class PhoneForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    address = StringField('Address')
    phone_number = StringField('Phone Number', validators=[InputRequired()])
    submit = SubmitField()