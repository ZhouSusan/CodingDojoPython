from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    apple_amt = request.form['apple']
    raspberry_amt = request.form['raspberry']
    strawberry_amt = request.form['strawberry']

    first_name =  request.form['first_name']
    last_name =  request.form['last_name']
    student_id = request.form['student_id']
    count = int(apple_amt) + int(raspberry_amt) + int(strawberry_amt)
    print(f"Charging {first_name} {last_name} for {count} fruits")
    return render_template("checkout.html", first_name=first_name, last_name=last_name,apple_amt=apple_amt,raspberry_amt=raspberry_amt,strawberry_amt=strawberry_amt, count=count, student_id=student_id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    