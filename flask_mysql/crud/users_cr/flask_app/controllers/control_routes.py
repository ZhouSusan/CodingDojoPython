from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_user import User

from flask_app.config.mysqlconnection import connectToMySQL

@app.route("/")
def index():
    users = User.get_all()
    return render_template("index.html", users=users)
            

@app.route('/users/create', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users/new')

@app.route('/users/new')
def users():
    users = User.get_all()
    return render_template("display_users.html", users=users)

@app.route('/')
def create_users():
    return redirect("/users/new")

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template("edit_user.html", user= user)

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/user/show/' + request.form['id'])

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data = {
        "id": id
    }
    User.destroy(data)
    return redirect('/users/new')

@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template("show_user.html", user=user)
