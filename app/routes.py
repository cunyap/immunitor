from flask import url_for, render_template, redirect
from flask import current_app as app
from .forms import ContactForm, SignupForm, StatusReport


@app.route('/')
def home():
    return render_template('index.html',
                           template='home-template')


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

@app.route('/status_report', methods=('GET','POST'))
def status_report():
    form = StatusReport()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('status_report.html',
                           form=form,
                           template='form-template')