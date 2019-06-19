from flask import Flask,render_template
import sqlite3

app = Flask(__name__)



@app.route('/')
def index():
    with sqlite3.connect("auto.db") as conn:
        conn.row_factory = dict_factory
        db = conn.cursor()
        rows = db.execute("SELECT * FROM mytable")
        # print(rows.fetchall())
        return render_template("index.html", rows = rows.fetchall())


if __name__ == '__main__':
    app.run()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d