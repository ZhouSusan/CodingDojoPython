from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_dojos import Dojo
from flask_app.models.model_ninjas import Ninja

from flask_app.config.mysqlconnection import connectToMySQL

@app.route("/dojos")
def index():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos = dojos)
            
@app.route('/dojo/show/<int:id>')
def show(id):
    data = { "id" : id}
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("display_all_ninjas_in_dojo.html", dojo=dojo)

@app.route('/ninja/new')
def new_ninja():
    return render_template("new_ninja.html", all_dojos=Dojo.get_all())

@app.route('/ninja/create', methods=["POST"])
def create_ninja():
    Ninja.save(request.form)
    dojo_id = request.form['dojo_id']
    return redirect('/dojo/show/' + str(dojo_id))

@app.route('/dojo/create', methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

