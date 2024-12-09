from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Selamat datang di aplikasi sederhana menggunakan Render! BY GROUP 07</h1>"

if __name__ == "__main__":
    app.run(debug=True)
