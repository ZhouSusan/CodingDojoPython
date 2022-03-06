from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say(name):
    return f"Hi {name}!"

@app.route('/repeat/<string:number>/<string:text>')
def repeat(number, text):
    output = ""
    for i in range(int(number)):
        output += text + " "
    return f"{output}"

@app.route('/<other>')
def no_reply(other):
    if other != dojo or greeter or repeat:
        print("Sorry! No response. Try again.")
        return "Sorry! No reponse. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.