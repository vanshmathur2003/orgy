from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello!</p>"

@app.route("/vansh")
def hello_vansh():
    return "<p>Hello, vansh!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
