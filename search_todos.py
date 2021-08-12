# Here the user can search for anything they want, using keywords for lists, tasks or even assignees

import sqlite3


def find_todo():
    print('\nSearch todos by list name, todo, or assignee\n'
          'To quite, type Q')
    database = 'bonus_todos.sqlite'
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    query = 'SELECT todo_id, task, assignee, due, todos.created, todo_lists.list ' \
            'FROM todos INNER JOIN todo_lists ON todo_lists.list_id = todos.list_id ' \
            'WHERE task LIKE ? OR assignee LIKE ? OR list LIKE ?'

    keyword = ''
    while not keyword:
        user = input('What are you looking for?...')
        if not user or not user.strip():
            print('Invalid entry, please try again.')
        elif user == 'Q':
            break
        else:
            keyword += user
            search_result = cur.execute(query, (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%')).fetchall()

            if len(search_result) > 0:
                for result in search_result:
                    print(f'ID #{result[0]}\n'
                          f'Task: {result[1]}\n'
                          f'Assignee: {result[2]}\n'
                          f'Due date: {result[3]}\n'
                          f'Created on: {result[4]}\n'
                          f'List: {result[5]}\n')
            else:
                print('No results matching your search were found')

            conn.commit()
            conn.close()
