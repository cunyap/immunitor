import json
from flask import url_for, render_template, redirect, make_response, request
from flask import current_app as app
from .forms import ContactForm, SignupForm, StatusReport, HiddenButton
from .interactive_fields import Status, ContributeMore, MoreInfo, KeepInTouch, QuestioningEverything
from datetime import datetime as dt

# @app.route('/')
# def home():
#     return render_template('index.html',
#                            template='home-template')

ID = dt.now().strftime('%c')



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
        elif 'immune' in request.form:
            s = "status_registered"
            status = "immune"
            save_info(ID=ID, key="status", value=status)
            return render_template('status.html',
                                   form=form,
                                   template='form-template',
                                   s="status_registered")
        elif 'non_infected' in request.form:
            s = "status_registered"
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

    if form.additional_info.validate(form):
        save_info(ID=ID, key="job", value=form.data['job'])
        save_info(ID=ID, key="age", value=form.data['age'])
        return redirect(url_for('success'))


    return render_template('status.html',
                           form=form,
                           template='form-template',
                           s="status_not_registered")

