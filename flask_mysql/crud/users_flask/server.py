from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all()
    return render_template("model_user.html", users=users)
            

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
    return render_template("edit.html", user= user)

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
    return render_template("show.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)