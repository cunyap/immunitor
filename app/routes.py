import json
from flask import url_for, render_template, redirect, make_response, request
from flask import current_app as app
#from .models import db, User
from .forms import ContactForm, SignupForm, StatusReport, HiddenButton
from .interactive_fields import TypeinField
from datetime import datetime as dt

# @app.route('/')
# def home():
#     return render_template('index.html',
#                            template='home-template')

ID = dt.now().strftime('%c')

@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('contact.html',
                           form=form,
                           template='form-template')


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    form = SignupForm()
    if form.validate_on_submit():
		# Here we will then insert the code which computes a hash if needed and starts uploading the data into our database
		# It will also trigger a reload of the live data or maybe this will only be done when one goes to the plotting page
        return redirect(url_for('success'))
    return render_template('signup.html',
                           form=form,
                           template='form-template')


@app.route('/success', methods=('GET', 'POST'))
def success():
    return render_template('success.html',
                           template='success-template')


@app.route('/email', methods=('GET','POST'))
def email():
    form = TypeinField()
    status="uff"
    print(str(status))

    if form.validate_on_submit():
        if 'infected' in request.form:
            status = "infected"
        elif 'immune' in request.form:
            status = "immune"
        save_info(ID=ID, status=status)
        return redirect(url_for('success'))
    return render_template('email.html',
                           form=form,
                           template='form-template')

def save_info(ID, status):
    with open("app/static/comments.json", 'r') as file:
        comments = json.load(file)
    comments[ID] = {}
    comments[ID]["status"] = status
    with open("app/static/comments.json", 'w') as outfile:
        json.dump(comments, outfile)


@app.route('/hiddenbutton', methods=('GET', 'POST'))
def hiddenbutton():
    form = HiddenButton()
    status = "duh"
    print(str(status))
    if form.validate_on_submit():
        status = "valid"
        print(str(status))
        if 'Age' in request.form:
            save_info(ID=ID, status="age")
        return redirect(url_for('success'))
    return render_template('hiddenbutton.html',
                               form=form,
                               template='form-template')
