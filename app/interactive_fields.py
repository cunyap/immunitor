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


class Status(FlaskForm):
    infected = SubmitField('Infected')
    immune = SubmitField('Immune')
    non_infected = SubmitField(' Non infected')


class ContributeMore(FlaskForm):
    yes = SubmitField('yes')
    no = SubmitField('no')

class MoreInfo(FlaskForm):
    submit = SubmitField('Submit')

    age = SelectField('Age', [DataRequired()],
                        choices=[('young', '0-50 years old'),
                                 ('old', '51-100 years old')])

    job = SelectField('Job', [DataRequired()],
                      choices=[('Wizard', 'Wizard'),
                               ('Witch', 'Witch'),
                               ('Muggle', 'Muggle')])


class KeepInTouch(FlaskForm):
    email = StringField('E-mail: ', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    submit = SubmitField('Submit')