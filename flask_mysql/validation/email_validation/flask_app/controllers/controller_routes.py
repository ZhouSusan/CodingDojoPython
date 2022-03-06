from flask_app import app
from flask import render_template,redirect,request,session,flash,url_for
from flask_app.models.model_email import Email

from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/email/create', methods=['POST'])
def create():
    print(request.form)
    if not Email.validate_email(request.form):
        return redirect('/')
    id = Email.save(request.form)
    return redirect(url_for('success', id = id))

@app.route('/success')
def success():
    data = {
        "id": request.args.get('id')
    }
    email = Email.get_one(data)
    return render_template("display_all.html", all_emails = Email.get_all(), email=email)

@app.route('/email/destroy/<int:id>')
def destroy(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect('/')