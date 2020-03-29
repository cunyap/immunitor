import json
from flask import url_for, render_template, redirect, make_response, request
from flask import current_app as app
from .forms import ContactForm, SignupForm, StatusReport, HiddenButton
from .interactive_fields import Status, ContributeMore, MoreInfo, KeepInTouch
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


@app.route('/status', methods=('GET','POST'))
def status():
    form = Status()
    if form.validate_on_submit():
        if 'infected' in request.form:
            status = "infected"
            save_info(ID=ID, key="status", value=status)
            return render_template('status.html',
                            form=form,
                            template='form-template',
                            s=1)
        elif 'immune' in request.form:
            status = "immune"
            save_info(ID=ID, key="status", value=status)
            return render_template('status.html',
                            form=form,
                            template='form-template',
                            s=1)
        elif 'non_infected' in request.form:
            status = "non_infected"
            save_info(ID=ID, key="status", value=status)
            return render_template('status.html',
                            form=form,
                            template='form-template',
                            s=1)

    return render_template('status.html',
                           form=form,
                           template='form-template',
                           s=0)


def save_info(ID, key, value):
    with open("app/static/comments.json", 'r') as file:
        comments = json.load(file)
    if ID not in comments.keys():
        comments[ID] = {}
    comments[ID][key] = value
    with open("app/static/comments.json", 'w') as outfile:
        json.dump(comments, outfile)


@app.route('/hiddenbutton', methods=('GET', 'POST'))
def hiddenbutton():
    form = HiddenButton()
    if form.validate_on_submit():
        print("yassss")
        if 'Age' in request.form:
            save_info(ID=ID, status="age")
        return redirect(url_for('success'))
    return render_template('hiddenbutton.html',
                               form=form,
                               template='form-template')


@app.route('/contribute_more', methods=('GET', 'POST'))
def contribute_more():
    form = ContributeMore()
    if form.validate_on_submit():
        if 'yes' in request.form:
            return redirect(url_for('more_info'))
        elif 'no' in request.form:
            return redirect(url_for('success'))
    return render_template('contribute_more.html',
                               form=form,
                               template='form-template')


@app.route('/more_info',  methods=('GET', 'POST'))
def more_info():
    form = MoreInfo()
    if form.validate_on_submit():
        if 'job' in request.form:
            save_info(ID=ID, key="job", value=form.data['job'])
        if 'age' in request.form:
            save_info(ID=ID, key="age", value=form.data['age'])
        if 'submit' in request.form:
            return redirect(url_for('keep_in_touch'))
    return render_template('more_info.html',
                           form=form,
                           template='form-template')

@app.route('/keep_in_touch', methods=('GET', 'POST'))
def keep_in_touch():
    form = KeepInTouch()
    if form.validate_on_submit():
        save_info(ID=ID, key="email", value=form.email.data)
        return redirect(url_for('success'))
    return render_template('keep_in_touch.html',
                           form=form,
                           template='form-template')
