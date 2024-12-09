from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! This is a Flask app deployed on Heroku. by Group 07"

if __name__ == "__main__":
    app.run()
