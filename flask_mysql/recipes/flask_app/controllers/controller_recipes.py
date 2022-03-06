from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe

from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/recipes/new')
def create_new():
    return render_template("new_recipe.html")

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/')
    data = {**request.form}
    data['user_id'] = session["user_id"]
    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def view_recipe(id):
    user = User.get_one({'id':session['user_id']})
    recipe = Recipe.get_one({'id': id})
    return render_template("show_recipe.html", recipe = recipe, user=user)

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    recipe = Recipe.get_one({'id': id})
    return render_template("edit_recipe.html", recipe=recipe)

@app.route('/recipes/update/<int:id>', methods=['POST'])
def update_recipe(id):
    data = {**request.form}
    data['id'] = id    
    Recipe.update(data)
    return redirect('/recipes/' + str(id))

@app.route('/recipes/delete/<int:id>')
def delete(id):
    Recipe.delete({'id':id})
    return redirect('/dashboard')
