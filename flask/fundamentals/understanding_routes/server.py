from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)       

@app.route('/')
def index():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    repeater = ""
    for idx in range(num):
        repeater += word + " "
    return repeater

@app.route('/<other>')
def no_reply(other):
    if other != dojo or other != say or other != repeat:
        return "Sorry! No response. Try again."

if __name__=="__main__": 
    app.run(debug=True)      