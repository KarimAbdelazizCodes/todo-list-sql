# Here the user can create new tasks. If they have no lists, they will be prompted to create one

import sqlite3
from datetime import datetime
from current_lists import show_current_lists


def new_todo():
    # This will show the user their current lists, in case they forgot the list names and IDs.
    # If the user has no lists, they are prompted to create a new list first, then add todos to it.
    print('Assign your task to a list by including the list ID\n'
          'To quit at any moment, type Q')
    show_current_lists()

    timestamp = datetime.now().strftime("%d-%b-%Y at %H:%M")
    database = 'bonus_todos.sqlite'
    conn = sqlite3.connect(database)
    cur = conn.cursor()

    query = 'INSERT INTO todos (list_id, task, assignee, due, created) ' \
            'VALUES (?, ?, ?, ?, ?)'

    list_id = ''
    while not list_id or not list_id.strip():
        enter_list_id = input('List ID:  ')
        if not enter_list_id or not enter_list_id.strip() or not enter_list_id.isdigit():
            print('Invalid entry. Try again.')
        else:
            list_id += enter_list_id

    task = ''
    while not task or not task.strip():
        enter_task = input('Task:  ')
        if not enter_task or not enter_task.strip():
            print('Invalid entry. Try again.')
        else:
            task += enter_task

    assignee = ''
    while not assignee or not assignee.strip():
        enter_assignee = input('Assignee:  ')
        if not enter_assignee or not enter_assignee.strip():
            print('Invalid entry. Try again.')
        else:
            assignee += enter_assignee

    due = ''
    while not due or not due.strip():
        enter_due = input('Due date:  ')
        if not enter_due or not enter_due.strip():
            print('Invalid entry. Try again.')
        else:
            due += enter_due

    # creates a tuple out of all user entries and dispatch them + timestamp tuple in line 54
    payload = (list_id, task, assignee, due)
    cur.execute(query, payload + (timestamp,))

    print('Done! :)')

    conn.commit()
    conn.close()
