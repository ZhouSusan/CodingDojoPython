from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_user import User

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/register/user', methods=['POST'])
def register():
    # validate the form here ...
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "username": request.form['username'],
        "password" : pw_hash
    }
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect("/dashboard")

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

    from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
@app.route('/register/user', methods=['POST'])
def register():
    # validate the form here ...
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "username": request.form['username'],
        "password" : pw_hash
    }
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect("/dashboard")

from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")


@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    return redirect('/dashboard')

flash("Email cannot be blank!", 'email')

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")