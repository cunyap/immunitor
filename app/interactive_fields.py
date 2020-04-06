from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField,
                     SubmitField,
                     SelectField,
                     FormField,
                     FileField)
from wtforms.validators import (DataRequired,
                                Email, ValidationError, Regexp)

countries = ['Afghanistan', 'Åland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, the Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, the Former Yugoslav Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine, State of', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']


class Status(FlaskForm):
    infected = SubmitField('Infected')
    immune = SubmitField('Immune')
    non_infected = SubmitField(' Non infected')


class Proof(FlaskForm):
    proof = StringField('Serial Number: ')
    proceed = SubmitField('Proceed')


class ContributeMore(FlaskForm):
    yes = SubmitField('Yes')
    no = SubmitField('No')


class MoreInfo(FlaskForm):

    def validate_country(form, field):
        if field.data not in countries:
            raise ValidationError('Not a valid country.')

    age = SelectField('Age', choices=[(str(i), str(i)) for i in range(0,120,1)])
    #age = StringField("Age: ", validators=[])
    gender = SelectField('Gender',
                         choices=[('-','-'),
                                  ('F', 'Female'),
                                  ('M', 'Male'),
                                  ('X', 'Other')])
    job = SelectField('Job',
                      choices=[('-','-'),
                               ('Teacher', 'Teacher'),
                               ('Health-care Worker', 'Health-care Worker'),
                               ('Construction Worker', 'Construction Worker'),
                               ('Academia', 'Academia')])
    country = StringField("Country: ", validators=[validate_country])
    postcode = StringField("Post Code: ", validators=[])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


class KeepInTouch(FlaskForm):
    email = StringField('E-mail: ', [
        Email(message='Not a valid email address.')])
    submit = SubmitField('Submit')


class ReturningUser(FlaskForm):
    image = FileField(u"Upload a screenshot or QR code picture: ")
    code = StringField('Or paste here the corresponding code: ')
    confirm = SubmitField('Confirm')
    return_landing = SubmitField('Return')


class QuestioningEverything(FlaskForm):
    proof = FormField(Proof)
    infection_status = FormField(Status)
    contribution = FormField(ContributeMore)
    additional_info = FormField(MoreInfo)


class QuestioningReturning(FlaskForm):
    retform = FormField(ReturningUser)







# class Country(object):
#
#     def __init__(self, message=None):
#         self.message = message
#
#     def __call__(self, form, field):
#         value = field.data
#         message = self.message
#         if message is None:
#             message = field.gettext('Invalid country name.')
#
#         if value not in countries:
#             raise ValidationError(message)