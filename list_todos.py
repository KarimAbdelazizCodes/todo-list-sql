# Here the user can either view all tasks in all lists, or view the tasks in a particular list

import sqlite3


def list_todos():
    database = 'bonus_todos.sqlite'
    conn = sqlite3.connect(database)
    cur = conn.cursor()

    # View all todos
    q1 = 'SELECT todo_id, task, assignee, due, todos.created, todo_lists.list ' \
         'FROM todos INNER JOIN todo_lists ON todo_lists.list_id = todos.list_id'

    # Todos from a specific list
    q2 = 'SELECT todo_id, task, assignee, due, todos.created, todo_lists.list ' \
         'FROM todos INNER JOIN todo_lists ON todo_lists.list_id = todos.list_id WHERE todos.list_id = ?'

    print('If you wish to view todos from a particular list, please type in the list ID\n'
          'Else, simply hit ENTER to view all todos')
    list_id = input('')
    if list_id:
        result = cur.execute(q2, (list_id,)).fetchall()
        if len(result) > 0:
            print(f'Todos in {result[0][5]} list:')
            for todo in result:
                print(f'ID #{todo[0]}\n'
                      f'Task: {todo[1]}\n'
                      f'Assignee: {todo[2]}\n'
                      f'Due date: {todo[3]}\n'
                      f'Created on: {todo[4]}\n')
        else:
            print('List is either empty or does not exist')
    else:
        result = cur.execute(q1).fetchall()
        if len(result) > 0:
            for todo in result:
                print(f'ID #{todo[0]}\n'
                      f'Task: {todo[1]}\n'
                      f'Assignee: {todo[2]}\n'
                      f'Due date: {todo[3]}\n'
                      f'Created on: {todo[4]}\n'
                      f'List: {todo[5]}\n')
        else:
            print('You currently have no todos')


