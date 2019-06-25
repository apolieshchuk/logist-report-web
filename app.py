from flask import Flask,render_template
import mysql.connector
app = Flask(__name__)



@app.route('/')
def index():
    conn = mysql.connector.connect(user='root', password='aipx123',
                                   host='localhost',port=3306,
                                   database='auto')
    cursor = conn.cursor()
    sql = "SELECT * FROM test"
    cursor.execute(sql)
    for (col1,col2,col3,col4) in cursor:
        print(col1,col2,col3,col4)
    return "Hello wotrld!"

    # with sqlite3.connect("auto.db") as conn:
    #     # conn.row_factory = sqlite3.Row
    #     cur = conn.cursor()
    #
    #     # шапка таблицы
    #     info = cur.execute("PRAGMA table_info(mytable)")
    #     head = [el[1] for el in info.fetchall()]
    #
    #     # ширина столбцов таблицы
    #     # TODO CSS
    #
    #     rows = cur.execute("SELECT * FROM mytable")
    #     # print(rows.fetchall())
    #     return render_template("index.html", rows = rows.fetchall(), head = head)


if __name__ == '__main__':
    app.run(debug=True)
