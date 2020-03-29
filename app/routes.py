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


@app.route('/')
def home():
    form = QuestioningEverything()
    if form.infection_status.validate_on_submit():
        if 'infected' in request.form:
            status = "infected"
            save_info(ID=ID, key="status", value=status)
            return render_template('status.html',
                                   form=form,
                                   template='form-template',
                                   s="status_registered")
        elif 'immune' in request.form:
            status = "immune"
            save_info(ID=ID, key="status", value=status)
            return render_template('status.html',
                                   form=form,
                                   template='form-template',
                                   s="status_registered")
        elif 'non_infected' in request.form:
            status = "non_infected"
            save_info(ID=ID, key="status", value=status)
            return render_template('status.html',
                                   form=form,
                                   template='form-template',
                                   s="status_registered")
    if form.contribution.validate_on_submit():
        if 'yes' in request.form:
            return render_template('status.html',
                                   form=form,
                                   template='form-template',
                                   c="contribution_y")
        if 'no' in request.form:
            return redirect(url_for('success'))

    if form.additional_info.validate_on_submit():
        save_info(ID=ID, key="job", value=form.data['job'])
        save_info(ID=ID, key="age", value=form.data['age'])
        return redirect(url_for('success'))


    return render_template('status.html',
                           form=form,
                           template='form-template',
                           s="status_not_registered")

