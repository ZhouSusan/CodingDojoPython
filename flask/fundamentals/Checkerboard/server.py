from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/') 
def index(color1=None, color2=None):
    return render_template("index.html", x=8, color1=color1, y=8, color2=color2)

@app.route('/<int:x>')
@app.route('/<int:x>/<string:color1>')
def custom_board_one(x, color1=None):
    return render_template("index.html", x=x, color1=color1, y=8)

@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<string:color1>/<int:y>/<color2>')
def third_board(x, y, color1=None, color2=None):
    return render_template("index.html", x=x,color1=color1, y=y, color2=color2)

if __name__=="__main__":   
    app.run(debug=True)  