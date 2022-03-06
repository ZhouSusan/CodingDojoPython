from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def display_blocks():
    return render_template("index.html", num=3)

@app.route('/play/<int:num>')
def repeat_blocks(num):
    return render_template("index.html", num=num)

@app.route('/play/<int:num>/<string:color>')
def change_color(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":     
    app.run(debug=True)    
