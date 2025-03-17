import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Nicole in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://basketball_table_user:VRw3UxZmBf8aIWLvK0kZvovyqxtHi3uB@dpg-cvc5uh23esus73ek78hg-a/basketball_table")
    conn.close()
    return "Database connection successful!"