from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/add')
def plus_method():
    a = request.args.get("a", 1)
    b = request.args.get("b", 1)
    result = float(a) + float(b)
    return "results : {}".format(result)

@app.route('/')
def hello():
    return "Welcome to python docker app example"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
