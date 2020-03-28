from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField,
                     TextAreaField,
                     SubmitField,
                     PasswordField,
                     DateField,
                     SelectField)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo,
                                Length,
                                URL)


class TypeinField(FlaskForm):
    email = StringField('E-mail: ', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    submit = SubmitField('Submit')
