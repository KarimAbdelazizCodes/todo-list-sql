# This is just the create the tables once
import sqlite3

database = 'bonus_todos.sqlite'
conn = sqlite3.connect(database)
cur = conn.cursor()

Q1 = 'CREATE TABLE todo_lists (list_id integer PRIMARY KEY, list TEXT UNIQUE NOT NULL, created TEXT)'

Q2 = 'CREATE TABLE todos (todo_id integer PRIMARY KEY, ' \
     'list_id integer NOT NULL, task TEXT NOT NULL, assignee TEXT NOT NULL, due TEXT, created TEXT,' \
     'FOREIGN KEY(list_id) REFERENCES todo_lists(list_id))'

cur.execute(Q1)
cur.execute(Q2)

conn.commit()
conn.close()
