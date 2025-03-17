#name: nicole cosmany
#date: 3.17.2025
#purpose: lab 10 website deployment using render 

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

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://basketball_table_user:VRw3UxZmBf8aIWLvK0kZvovyqxtHi3uB@dpg-cvc5uh23esus73ek78hg-a/basketball_table")
    cur = conn.cursor()
    #create the basketball table with the following attributes 
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
''')
    conn.commit()
    conn.close()
    return "Basketball table successfully created!"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://basketball_table_user:VRw3UxZmBf8aIWLvK0kZvovyqxtHi3uB@dpg-cvc5uh23esus73ek78hg-a/basketball_table")
    cur = conn.cursor()
    #insert the following rows into the basketball table 
    cur.execute( '''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgresql://basketball_table_user:VRw3UxZmBf8aIWLvK0kZvovyqxtHi3uB@dpg-cvc5uh23esus73ek78hg-a/basketball_table")
    cur = conn.cursor()
    #select everything from the basketball table 
    cur.execute ( '''
    SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    #display outputs by adding table elements to response_string
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string +="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+= "</table>"
    return response_string

@app.route('/db_drop')
def def_drop():
    conn = psycopg2.connect("postgresql://basketball_table_user:VRw3UxZmBf8aIWLvK0kZvovyqxtHi3uB@dpg-cvc5uh23esus73ek78hg-a/basketball_table")
    cur = conn.cursor()
    #remove basketball table
    cur.execute('''
    DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully dropped!"