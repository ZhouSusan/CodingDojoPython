flask check list

#1.open up terminal
#2. type pip install pipenv
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
#templates- add html file
#static-css(style.css)-js-(script.js)-img(images)
#8. test server

#exit when closing- exit