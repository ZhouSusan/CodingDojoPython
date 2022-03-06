from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_survey import Survey

from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    if not Survey.validate_survey(request.form):
        return redirect('/')
    Survey.save(request.form)
    return redirect('/results')

@app.route('/results')
def result():
    survey = Survey.get_last_survey() 
    return render_template('results.html', survey=survey)

@app.route('/back')
def back():
    session.clear()
    return redirect('/')
