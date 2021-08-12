# Here the user can create new lists

import sqlite3
from datetime import datetime


def new_list():
    timestamp = datetime.now().strftime("%d-%b-%Y at %H:%M")
    database = 'bonus_todos.sqlite'
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    query = 'INSERT INTO todo_lists (list, created) ' \
            'VALUES (?, ?)'

    print('To quit, type Q')

    list_name = ''
    while not list_name:
        user = input('List name:  ')
        if not user or not user.strip():
            print('Please enter a valid name')
        elif user == 'Q':
            break
        else:
            list_name += user
            cur.execute(query, (list_name, timestamp))
            q2 = cur.execute('SELECT * FROM todo_lists ORDER BY list_id DESC LIMIT 1').fetchone()
            print(f'List {q2[1]} has been created, list ID is {q2[0]}')

            conn.commit()
            conn.close()

