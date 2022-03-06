from flask import Flask, render_template 
app = Flask(__name__)   

@app.route('/') 
def orgininal_board():
    return render_template("index.html", x=8, y=8)

@app.route('/<int:x>')
@app.route('/<int:x>/<string:color1>')
def second_board(x, color1=None):
    return render_template("index.html", x=x, color1=color1, y=8)

@app.route('/<int:x>/<string:color1>/<int:y>/<color2>')
def third_board(x, color1, y, color2):
    return render_template("index.html", x=x,color1=color1, y=y, color2=color2)

if __name__=="__main__":
    app.run(debug=True)