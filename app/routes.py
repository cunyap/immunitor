import json
from flask import url_for, render_template, redirect, make_response, request, session, Response
from flask import current_app as app
from werkzeug.utils import secure_filename
from .interactive_fields import Status, ContributeMore, MoreInfo, KeepInTouch, QuestioningEverything, ReturningUser, QuestioningReturning
from datetime import datetime as dt
from .utils import get_data_from_json
from .visualization import create_plot
from .openbis import (establish_db_connection, get_all_cases, register_new_case, update_case)
from pyzbar.pyzbar import decode
from PIL import Image
import os

# @app.route('/')
# def home():
#     return render_template('index.html',
#                            template='home-template')
#                            template='home-template')

# ID = dt.now().strftime('%c')
# ID = session['_id']

ID = 0


@app.route('/success', methods=('GET', 'POST'))
def success():
    return render_template('success.html',
                           template='success-template',
                           scrollToAnchor='success')


def create_infofile(ID):
    f = open("app/static/{}.json".format(ID.decode("utf-8")), "w+")
    f.write('{}')


def save_info(ID, key, value):
    with open("app/static/{}.json".format(ID.decode("utf-8")), 'r') as file:
        comments = json.load(file)
    comments[key] = value
    with open("app/static/{}.json".format(ID.decode("utf-8")), 'w+') as outfile:
        json.dump(comments, outfile)


@app.route('/returning', methods=('GET', 'POST'))
def returning():
    form = ReturningUser()
    global ID
    if form.validate_on_submit():
        if 'confirm' in request.form:
            file = form.image.data
            filename = secure_filename(file.filename)
            if filename:
                d = decode(Image.open(file))
                if d:
                    ID = d[0].data
                    print(ID)
                    create_infofile(ID)
                    return redirect(url_for('status'))
                else:
                    return render_template('returning.html',
                                           form=form,
                                           template='base',
                                           scrollToAnchor='warningNoFile',
                                           error='noQR')
            else:
                return render_template('returning.html',
                                       form=form,
                                       template='base',
                                       scrollToAnchor='warningNoFile',
                                       error='noFile')
        elif 'return_landing' in request.form:
            return redirect(url_for('landing'))

    return render_template('returning.html',
                           form=form,
                           template='base')


@app.route('/status', methods=('GET', 'POST'))
def status():
    form = QuestioningEverything()
    # if 'returning-submit' in request.form:
    #     # d = decode(Image.open("app/static/img/qrtest.png"))
    #     # print(d)
    #     file = form.returning.image.data
    #     filename = secure_filename(file.filename)
    #     #img = file.save(os.path.join(app.instance_path, 'qr_codes', filename))
    #     d = decode(Image.open(file))

    if 'proof-proceed' in request.form:
        save_info(ID=ID, key="testid", value=form.proof.data['proof'])
        return render_template('status.html',
                               form=form,
                               template='form-template',
                               p="proof_submitted",
                               scrollToAnchor="proceed")

    # if form.infection_status.validate(form):
    if 'infection_status-infected' in request.form:
        status = 1
        save_info(ID=ID, key="diagnostic", value=status)
        return render_template('status.html',
                               form=form,
                               template='base',
                               p="proof_submitted",
                               s="status_registered", scrollToAnchor='infected')
    elif 'infection_status-immune' in request.form:
        status = 2
        save_info(ID=ID, key="diagnostic", value=status)
        return render_template('status.html',
                               form=form,
                               template='base',
                               p="proof_submitted",
                               s="status_registered", scrollToAnchor='immune')
    elif 'infection_status-non_infected' in request.form:
        status = 0
        save_info(ID=ID, key="diagnostic", value=status)
        return render_template('status.html',
                               form=form,
                               template='base',
                               p="proof_submitted",
                               s="status_registered", scrollToAnchor='nonInfected')

    # if form.contribution.validate(form):
    if 'contribution-yes' in request.form:
        return render_template('status.html',
                               form=form,
                               template='base',
                               p="proof_submitted",
                               s="status_registered",
                               c="contribution_y", scrollToAnchor="contributeMore")
    if 'contribution-no' in request.form:
        permID = get_data(ID)
        return redirect(url_for('success', permID=permID))

    if 'additional_info-submit' in request.form:
        save_info(ID=ID, key="job", value=form.additional_info.data['job'])
        save_info(ID=ID, key="age", value=int(form.additional_info.data['age']))
        save_info(ID=ID, key="country", value=form.additional_info.data['country'])
        if form.additional_info.data['postcode']:
            save_info(ID=ID, key="zip", value=int(form.additional_info.data['postcode']))
        # return redirect(url_for('success'), perm_id=get_data(ID))
        # if recaptcha.verify():
        permID = get_data(ID)
        return redirect(url_for('success', permID=permID))

    return render_template('status.html',
                           form=form,
                           template='base',
                           s="status_not_registered", scrollToAnchor="proceed")


@app.route('/geojson-features', methods=['GET'])
def get_all_points():
    d, df, ddf, _ = get_data_from_json()
    return Response(ddf, mimetype='application/json')


@app.route('/visuals')
def visuals():
    _, df, _, _ = get_data_from_json()
    graphJSON = create_plot(df)
    return render_template('visuals.html',
                           template='signup-template', plot=graphJSON, scrollToAnchor='visuals')

@app.route('/')
def main():
    return redirect(url_for('landing'))


@app.route('/index', methods=('GET', 'POST'))
def index():
    form = ReturningUser()
    global ID
    if form.validate_on_submit():
        if 'confirm' in request.form:
            file1 = open(
                "C:\\Users\\Localadmin\\ownCloud\\SoftwareDev\\Python\\flask_demo\\codevscovid19_app\\app\\myfile.txt",
                "w+")
            # \n is placed to indicate EOL (End of Line)
            file1.write("Hello \n")
            file1.writelines(form.image.data)
            file1.close()
            file = form.image.data
            # filename = secure_filename(file.filename)
            if file is not None:
                file1 = open("C:\\Users\\Localadmin\\ownCloud\\SoftwareDev\\Python\\flask_demo\\codevscovid19_app\\app\\myfile.txt", "w+")
                # \n is placed to indicate EOL (End of Line)
                file1.write("Hello \n")
                file1.writelines(file)
                file1.close()
                # d = decode(Image.open(file))
                # ID = str(d[0].data)
                # print(ID)
                # create_infofile(ID)
                return redirect(url_for('status#newUser'))
            else:
                print('error')
        elif 'new_user' in request.form:
            ID = "test_user"
            create_infofile(ID)
            return redirect(url_for('status#newUser'))
    return render_template('returning.html',
                           form=form,
                           template='base')


@app.route('/terms')
def terms():
    return render_template('terms.html', template='base', scrollToAnchor='terms')


@app.route('/faq')
def faq():
    return render_template('faq.html', template='base', scrollToAnchor='faq')

@app.route('/batch')
def batch():
    return render_template('batch.html', template='base', scrollToAnchor='batch')

@app.route('/landing')
def landing():
    return render_template('info.html', template='base')

@app.route('/info')
def info():
    return render_template('info.html', template='base', scrollToAnchor='start')


def get_data(ID):
    with open("app/static/{}.json".format(ID.decode("utf-8")), 'r') as file:
        comments = json.load(file)
    o = establish_db_connection()
    perm_id = register_new_case(o=o, data=comments)
    return perm_id
