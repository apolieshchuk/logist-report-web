from flask import Flask,render_template
import mysql.connector

from static import COLUMNS_AUTO

app = Flask(__name__)
application = app 


@app.route("/")
def hello():
    conn = mysql.connector.connect(user='aipx', password='Fleepaipx1203',
                                  host='91.239.232.46',port = 3306,
                                  database = 'aipx_logrep')
    cursor = conn.cursor()
    
    # шапка таблицы
    cursor.execute("SHOW columns FROM auto")
    head = [el[0] for el in cursor.fetchall() if el[0] in COLUMNS_AUTO]

    # записи
    s = ",".join(COLUMNS_AUTO)
    cursor.execute(f"SELECT {s} FROM auto")
    records = cursor.fetchall()
    return render_template("index.html", records=records, head=head)

if __name__== "__main__":
    app.run(debug=True)