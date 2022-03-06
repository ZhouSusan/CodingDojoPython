from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_dojos import Dojo

from flask_app.config.mysqlconnection import connectToMySQL


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['language'] = request.form['language']
    session['location'] = request.form['location']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def result():
    return render_template('results.html')

@app.route('/back')
def back():
    session.clear()
    return redirect('/')
