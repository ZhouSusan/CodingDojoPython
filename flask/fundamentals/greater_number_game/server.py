import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)       
app.secret_key = 'keep it secret, keep it safe'  


@app.route('/')
def home():
    if "num" not in session:
        session['num'] = random.randint(1, 100)
        session['guess'] = 0
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    print(request.form)
    guess = request.form['guess']
    session['guess'] = int(guess)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__": 
    app.run(debug=True)   