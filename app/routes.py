import json
from flask import url_for, render_template, redirect, make_response, request, session, Response
from flask import current_app as app
from .forms import ContactForm, SignupForm, StatusReport, HiddenButton
from .interactive_fields import Status, ContributeMore, MoreInfo, KeepInTouch, QuestioningEverything
from datetime import datetime as dt
from .utils import get_data_from_json
from .visualization import create_plot

# @app.route('/')
# def home():
#     return render_template('index.html',
#                            template='home-template')

ID = dt.now().strftime('%c')
#ID = session['_id']



@app.route('/success', methods=('GET', 'POST'))
def success():
    return render_template('success.html',
                           template='success-template')





def save_info(ID, key, value):
    with open("app/static/comments.json", 'r') as file:
        comments = json.load(file)
    if ID not in comments.keys():
        comments[ID] = {}
    comments[ID][key] = value
    with open("app/static/comments.json", 'w') as outfile:
        json.dump(comments, outfile)

@app.route('/status', methods=('GET', 'POST'))
def home():
    form = QuestioningEverything()
    if form.infection_status.validate(form):
        if 'infection_status-infected' in request.form:
            status = "infected"
            save_info(ID=ID, key="status", value=status)
            return render_template('status.html',
                                   form=form,
                                   template='form-template',
                                   s="status_registered")
        elif 'infection_status-immune' in request.form:
            status = "immune"
            save_info(ID=ID, key="status", value=status)
            return render_template('status.html',
                                   form=form,
                                   template='form-template',
                                   s="status_registered")
        elif 'infection_status-non_infected' in request.form:
            status = "non_infected"
            save_info(ID=ID, key="status", value=status)
            return render_template('status.html',
                                   form=form,
                                   template='form-template',
                                   s="status_registered")
    if form.contribution.validate(form):
        if 'contribution-yes' in request.form:
            return render_template('status.html',
                                   form=form,
                                   template='form-template',
                                   s="status_registered",
                                   c="contribution_y")
        if 'contribution-no' in request.form:
            return redirect(url_for('success'))

    if 'additional_info-submit' in request.form:
        save_info(ID=ID, key="job", value=form.additional_info.data['job'])
        save_info(ID=ID, key="age", value=form.additional_info.data['age'])
        save_info(ID=ID, key="country", value=form.additional_info.data['country'])


    return render_template('status.html',
                           template='form-template',
                           s="status_not_registered")



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
