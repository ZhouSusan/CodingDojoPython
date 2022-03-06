from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_user import User

from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/')
def home():
    return render_template("index.html")