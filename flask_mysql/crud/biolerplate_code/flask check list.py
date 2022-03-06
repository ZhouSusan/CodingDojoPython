flask check list

#1.create a new folder
#2. open up terminal
#2. pipenv install flask pymysql flask-bcrypt
#3.check for pipelock, pip.file
#4. create server.py
#5. run pipenv shell
#6. set up routes



<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='/css/style.css') }}">

<script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>

<img src="{{ url_for('static', filename='my_img.png') }}">

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)       
app.secret_key = 'keep it secret, keep it safe'              

"""
@app.route('/')                 This will change           
def hello_world():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html')  
"""

if __name__=="__main__": 
    app.run(debug=True)      

#7. create file structure
    """
    flask_app folder
        -__init__.py
        -config
            -mysqlconnection.py
        -controllers
            -controller_routes.py
        -models
            -model_user.py
        -static
            -css
                -style.css
            -js
                -script.js
            -img
        -templates    
    """
#exit when closing- exit when leaving server 

#8. create html template
#9. python server.py

