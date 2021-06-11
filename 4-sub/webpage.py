from flask import Flask
app = Flask(__name__)

@app.route("/python")
def homepage():
    return "<h1> hello, World! </h1>"

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)