#What is Flask?
#A microframework for creating web applications easily with Python
#Supports CRUD

#Create - POST(Creates the object on every request) and PUT (Only on first request)
#GET
#UPDATE
#DELETE

#How to start?
#1 pip install flask
#2 import flask
from flask import Flask
#3 instantiate flask
app = Flask("My first Application")
#4 run the app
@app.route('/')

#5 create a method to be accessed
def hello():
    return 'Hello World!'

#6 add condition to only run app if the name of the app is main
if __name__ == "__main__":
    app.run(debug=True)

#7 start the server as any other python app.






