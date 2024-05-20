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

export FLASK_APP=app.py
export FLASK_ENV=development

#Run the flask app

flask run 

#(por defecto corre en puerto 5000)

#Se puede pasar --app para identificar el archivo a correr
#Se puede usar --debug para iniciar en modo debug (reinicia si los archivos cambiaron)

#RETURNING JSON
#Retornar un tipo serializable

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return {"message":"Hello world"}




