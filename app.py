from flask import Flask, g, render_template
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

@app.route("/")
def home():
    return "<h1>Selamat datang di aplikasi sederhana menggunakan Render! BY GROUP 07</h1>"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/data")
def data():
    cur = get_db().cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO test (name) VALUES ('Test User')")
    get_db().commit()
    return "Data added to database!"

# Halaman Tentang Kami
@app.route("/about")
def about():
    group_members = [
        {"name": "Indriana Noviyanti", "image": "indriana.jpg", "bio": "Pecinta desain dan seni, berkontribusi pada kreativitas tim."},
        {"name": "Farhan Rangkuti", "image": "farhan.jpg", "bio": "Pengembang backend, spesialis algoritma."},
        {"name": "Bhagas Ade Pramono", "image": "bhagas.jpg", "bio": "Ahli dalam sistem jaringan, menyatukan koneksi antar sistem."},
        {"name": "Kardina Ferlinda", "image": "kardina.jpg", "bio": "Pengembang frontend, membangun antarmuka yang menarik."}
    ]
    return render_template("about.html", members=group_members)


if __name__ == "__main__":
    app.run(debug=True)
