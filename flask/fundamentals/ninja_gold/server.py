from flask import Flask, render_template, request, redirect, session
import random 
from datetime import datetime

app = Flask(__name__)       
app.secret_key = 'keep it secret, keep it safe' 

date = datetime.now()

@app.route('/')
def index():
    if "total" not in session:
        session['total'] = 0
    session['message'] = ""
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    if building == 'farm':
        num = random.randint(10,12)
        session['total'] += num
        session['message'] += f"Earned {num} golds from the farm! {str(date)}\n"
    elif building == 'cave':
        num = random.randint(5, 10)
        session['total'] += num
        session['message'] += f"Earned {num} golds from the cave! {str(date)}\n"
    elif building == 'house':
        num = random.randint(2,5)
        session['total'] += num
        session['message'] += f"Earned {num} golds from the house! {str(date)}\n"
    else:
        num = random.randint(-50,50)
        if (num < 0):
            session['message'] += f"Entered a casino and lost {num} golds..ouch.. {str(date)}\n"
        else:
           session['message'] += f"Earned {num} golds from the casino! {str(date)}\n"  
        session['total'] += num        
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__": 
    app.run(debug=True)  