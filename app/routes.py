from flask import url_for, render_template, redirect, jsonify, Response
from flask import current_app as app
from .forms import ContactForm, SignupForm
from .utils import get_data_from_json
from .visualization import create_plot
import json



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


@app.route('/geojson-features', methods=['GET'])
def get_all_points():

    d, df = get_data_from_json()
    return Response(d, mimetype='application/json')


@app.route('/visuals')
def main():
    _, df = get_data_from_json()
    print(df)
    graphJSON = create_plot(df)
    return render_template('visuals.html',
                           template='signup-template', plot=graphJSON)
