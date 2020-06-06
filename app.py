from flask import Flask, escape, request
import os

app = Flask(__name__)


@app.route('/add/<int:A>/<int:B>')
def plus_method(A, B):
    result = A + B
    return '{ "A" : ' + str(A) + ', "B" : ' + str(B) + ', "result" : ' + str(result) + '}'


@app.route('/')
def hello():
    return "Welcome to python docker app example"


@app.route('/env')
def printEnvVar():
    printvar = os.environ['MYVAR']
    return '{"env_var" : ' + printvar + '}'


if __name__ == "__main__":
    port = int(os.environ.get('PORT',3000))
    app.run(host="0.0.0.0", port = port)
