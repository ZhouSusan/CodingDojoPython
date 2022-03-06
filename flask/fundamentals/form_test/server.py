from flask import Flask, render_template, request, redirect
app = Flask(__name__) 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process_form', methods=['POST'])
def process_form():
    print(request.form)
    data = {
        **request.form
    }
    print(data)
    return redirect('/success')

@app.route('/success')
def success():
    return render_template("success.html")

if __name__=="__main__":
    app.run(debug=True) 