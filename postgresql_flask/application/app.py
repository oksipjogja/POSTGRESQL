import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)
# ...


@app.route('/create/', methods=['POST'])
def create():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = request.form['pages_num']
        review = request.form['review']
        cur.execute("INSERT INTO books (title, author, pages_num, review) VALUES (%s,%s,%s,%s)", (title, author, pages_num, review))
        conn.commit()
        flash('Book Added successfully')
        return redirect(url_for('Index'))
