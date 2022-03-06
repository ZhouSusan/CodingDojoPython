from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)    
app.secret_key = "shhhh shhhh shhh"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    return render_template("index.html")

@app.route('/add')
def add():
    session['count'] += 1 
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session.clear()		   		
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['count'] += 2
    return redirect('/')

@app.route('/increment', methods=['Post'])
def resetting():
    num = request.form['increment']
    num = int(num)
    session['count'] += num 
    return redirect('/')

if __name__=="__main__":  
    app.run(debug=True)