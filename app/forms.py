"""Form class declaration."""
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


class ContactForm(FlaskForm):
    """Contact form."""

    name = StringField('Name', [
        DataRequired()])
    email = StringField('Email', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    body = TextAreaField('Message', [
        DataRequired(),
        Length(min=4, message='Your message is too short.')])
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    """Sign up for a user account."""

    email = StringField('Email', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    password = PasswordField('Password', [
        DataRequired(message="Please enter a password."),
    ])
    confirmPassword = PasswordField('Repeat Password', [
            EqualTo(password, message='Passwords must match.')
            ])
    title = SelectField('Title', [DataRequired()],
                        choices=[('Farmer', 'farmer'),
                                 ('Corrupt Politician', 'politician'),
                                 ('No-nonsense City Cop', 'cop'),
                                 ('Professional Rocket League Player', 'rocket'),
                                 ('Lonely Guy At A Diner', 'lonely'),
                                 ('Pokemon Trainer', 'pokemon'),
                                 ('Desperate housewife', 'wife')])
    website = StringField('Website', validators=[URL()])
    birthday = DateField('Your Birthday')
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


class StatusReport(FlaskForm):
    """
    Declare your status: infected, not infected, immune
    """
    status_not_infected = SubmitField('Not infected')
    status_infected = SubmitField('blu')
    status_immune = SubmitField('Immune')

# class StatusReport(FlaskForm):
#     """Infected etc."""
#     status_infected = SubmitField('Infected')
#     status_immune = SubmitField('Immune')
#     status_noinf = SubmitField('Not')


class HiddenButton(FlaskForm):
    """Infected"""
    status_noninfected = SubmitField('Non Infected')
    status_infected = SubmitField('bla')
    status_immune = SubmitField('Immune')

    age_text = SubmitField('Age')
    job_text = SubmitField('Job')
    location_text = SubmitField('Location')
    email_text = SubmitField('Email')

    title = SelectField('Age', [DataRequired()],
                        choices=[('AgeY', '0-50 years old'),
                                 ('AgeO', '51-100 years old')])
