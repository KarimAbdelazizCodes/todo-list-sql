# This will show the user how many lists they have, and how many tasks are in each list

import sqlite3
from create_todo_list import new_list


def show_current_lists():
    database = 'bonus_todos.sqlite'
    conn = sqlite3.connect(database)
    cur = conn.cursor()

    query = 'SELECT * FROM todo_lists'

    # This will count the number of todos in each list - used on line 19
    query2 = 'SELECT COUNT(list_id) from todos WHERE list_id = (?)'

    result = cur.execute(query).fetchall()
    if len(result) > 0:
        print('\nThese are your current lists:')
        for list in result:
            count = cur.execute(query2, (list[0],)).fetchone()
            print(f'{list[1]}, ID: {list[0]} -- Number of todos: {count[0]}\n'
                  f'Created on: {list[2]}\n')
    else:
        print('\nIt looks like you have no todo lists\n'
              'Let\'s create one now!\n')
        new_list()
