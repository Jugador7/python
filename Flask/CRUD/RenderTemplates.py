
#Rendering templates
#import render_template. 

#How to start?
#1 pip install flask
#2 import flask
from flask import Flask, render_template, request
#3 instantiate flask
app = Flask("My first Application")

#4 run the app
@app.route('/sample')
#5 create a method to be accessed
def getSampleHtml():
    return render_template('sample.html')

#4 run the app
@app.route('/user/<username>', methods=['GET'])
#5 create a method to be accessed
def greetUser(username):
    return render_template('result.html', username=username)

#4 run the app
@app.route('/user', methods=['GET'])
#5 create a method to be accessed
def greetUserBasedOnReq():
    username = request.args.get("username")
    return render_template('result.html', username=username)

#6 add condition to only run app if the name of the app is main
if __name__ == "__main__":
    app.run(debug=True)

#7 start the server as any other python app.