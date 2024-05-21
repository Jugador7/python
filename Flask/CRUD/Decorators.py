#How to start?
#1 pip install flask
#2 import flask
from flask import Flask, render_template, request
#3 instantiate flask
app = Flask("My first Application")

#Decorators help in annotating the methods and tell what a particular method is meant for. 
#These are different from comments. This is used by the interpreter while running the code.
#Let’s say we have a python code where we want all the output to be in JSON format. 
#It doesn’t make sense to include code for these in each of the methods 
#as it makes the lines of code redundant. 
#In such cases, we can handle this with a decorator.
#As you can see the method call has been wrapped with the decorator. 
#The coder has a free will to choose the name of the decorator. 
#Here the name chosen is jsonify_decorator.

def jsonify_decorator(function):
    def modifyOutput():
        return {"output":function()}
    return modifyOutput
@jsonify_decorator
def hello():
    return 'hello world'
@jsonify_decorator
def add():
    num1 = input("Enter a number - ")
    num2 = input("Enter another number - ")
    return int(num1)+int(num2)
print(hello())
print(add())

#@app.route(“/“) is a Python decorator that Flask provides to assign 
#URLs in our app to functions easily. 
#You can easily tell that the decorator is telling our 
#@app that whenever a user visits our application’s domain, in our case, 
#execute the home() function.

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return "Hello World!"

#For example, to get the details of a user whose userId is U0001, you may go to
#http://mydomain.com/userdetails/U0001.
#It doesn’t make sense to define a different route for each user you may be dealing with. 
#In such cases, we define the route like this.

@app.route("/userdetails/<userid>")
def getUserDetails(userid):
    return "User Details for  "+userid