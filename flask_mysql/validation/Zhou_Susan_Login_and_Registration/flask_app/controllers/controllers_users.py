from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_users import User
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/create/user', methods=['POST'])
def create_user():
    print(request.form)
    if not User.validate_user(request.form):
        return redirect('/')
    if not User.validate_email(request.form):
        return redirect('/')
    data = {**request.form}
    data['password'] = bcrypt.generate_password_hash(data['password'])
    print(data['password'])
    id = User.save(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/login',  methods=['POST'])
def login():
    data = {
        "email": request.form["email"]
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    elif not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/dashboard')
def results():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    user= User.get_one(data)
    return render_template("success.html", user= user )

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
