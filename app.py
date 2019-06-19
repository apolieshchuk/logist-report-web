from flask import Flask,render_template
import sqlite3

app = Flask(__name__)



@app.route('/')
def index():
    with sqlite3.connect("auto.db") as conn:
        # conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        # шапка таблицы
        info = cur.execute("PRAGMA table_info(mytable)")
        head = [el[1] for el in info.fetchall()]

        # ширина столбцов таблицы
        # TODO CSS

        rows = cur.execute("SELECT * FROM mytable")
        # print(rows.fetchall())
        return render_template("index.html", rows = rows.fetchall(), head = head)


if __name__ == '__main__':
    app.run(debug=True)
