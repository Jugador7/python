#use Requests library

from flask import Flask, escape
import requests

app = Flask(__name__)

@app.route("/")
def get_author():
    res = requests.get("")
    if res.status_code == 200:
        return {"message" : res.JSON()}
    elif res.status_code == 404:
        return{"message" : "Something went wrong!"}, 404
    else:
        return{"message": "Server error"}, 500
    

#Dynamic route parameters
#Si quiero usar el mismo endpoint para responder para todos los recursos (ie. ISBN)

@app.route("/book/<isbn>")
def get_author(isbn):
    res = requests.get("//openlibrary.org/isbn/{escape(isbn)}.JSON")
    if res.status_code == 200:
        return {"message" : res.JSON()}
    elif res.status_code == 404:
        return{"message" : "Something went wrong!"}, 404
    
#Examples
#Parameter types validate requests
#@app.route("terminals/<string:airport_code>")
#@app.route("/book/<int:isbn>")
#@app.route("/network/<uuid:uuid>")
def uuid(uuid):
    res = requests.get("//openlibrary.org/isbn/{uuid}.JSON")
