#Creating a Flask application
#1 Install Flas
#2 Create the main server file (app.py)

from flask import Flask
app = Flask(__name__)

#ROUTES
#use the @app decorator to define the method
#Pass in the URL path
#Return the HTML in the method

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "<b>My first Flasl application in action"

#Running Flask
#1. FLASK_APP (name of the main server file)
#2. FLASK_ENV (se deprecará en Flask 2.3)

#En gitbash de Windows correr set FLASK_APP=app.py
# En linux correr export FLASK_APP=app.py
#export FLASK_ENV=development

#Run the flask app

#flask run 

#(por defecto corre en puerto 5000)

#Se puede pasar --app para identificar el archivo a correr
#Se puede usar --debug para iniciar en modo debug (reinicia si los archivos cambiaron)


#Mode debug
#flask --app app --debug run

#RETURNING JSON
#1Retornar un tipo serializable

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return {"message":"Hello world"}

#2Usar el método Jsonify
#pasar los pares llave:valor
#retornar el JSON al cliente

from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def index():
  return jsonify (message = "Hello world")

if __name__ == '__main__':
    app.run(debug=True)

#ENV define el entorno
#DEBUG
#TESTING
#SECRET_KEY firma la cookie de la sesión
#SESSION_COOKIE_NAME
#SERVER_NAME
#JSONIFY_MIMETYPE

#LoadApp configuration

app.config["SECRET_KEY"] = "random-secret-key"

#Configure from an environment variable

app.config["VARIABLE_NAME"]
app.config.from_prefixed_emv()