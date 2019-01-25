#flaskblog.py
from flask import Flask
app = Flask(__name__)

@app.route("/")

@app.route("/Welcome to Gold-Schudler!")
def home():
    return "<h1>Home Page!</h1>"


@app.route("/about")
def about():
    return "<h1>Nothing is here!</h1>"


if __name__ == '__main__':
	app.run(debug = True)



# export FLASK_APP=flaskblog.py
# flask run