
from flask import Flask,jsonify,request
app = Flask(__name__)
prueba=[{"nombre":"Miguel Jimenez", "sexo": "m"},{"nombre":"Pedro", "sexo": "m"}]
@app.route('/')
def hello_world():

    return jsonify(prueba)

@app.route('/webhouck/<name>')
def webhouck(name=None):
    return name


app.run(port=3001,debug=True)

