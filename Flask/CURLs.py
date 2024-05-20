#Estos dos métodos hacen lo mismo

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

@app.route("/health", methods= ["GET"])
def health():
    return jsonify(dict(status="OK")), 200

#Ejemplo de refactorización para usar varios métodos.

@app.route("/health", methods= ["GET, POST"])
def health():
    if request.method == "GET": return jsonify(status="OK", method = "GET"), 200
    if request.method == "POST": return jsonify(status="OK", method = "POST"), 200

#All HTTP calls to Flask contain the request object created from Flask.Request class. 

#Common request attributes are: server, headers, URL, access_route, full_path, is_secure, is_JSON, cookies. 

#The header contains: Cache-control, Accept, Accept-Encoding, User-Agent,  Accept-Language, Host

#Request object Methods:
#get_data: Get POST data from the request as bytes
#get_JSON: Parses POST data from the request as JSON

#Parse request data:
#args: MultiDict[str,str] give us request data as a dictionary
#JSON: Optional[Any]
#files: ImmutableMultiDict[str, FileStorage] - provides all user uploaded files
#form: ImmutableMultiDict[str, str] - contains all values posted in a form submission
#values: CombinedMultiDict[str,str] - Combines args data with formData
#Example:
from flask import Flask, request
app = Flask(__name__)

@app.route("/health")
def helloworld():
    course = request.args["course"]
    rating = request.argfs.get("rating")
    return {"message" : f"{course} with rating {rating}"}

#Flask has an in-built response class you can leverage on to give a response back to the client
#Common response attributes:
#status_code, headers, content_type, content_length, content_encoding, mimetype, expires

#common methods of response objects
#set_cookie, delete_cookie

#Usage methods:
#JSONify, make_response, redirect, abort



