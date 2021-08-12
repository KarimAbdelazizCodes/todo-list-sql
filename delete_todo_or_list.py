# Here the user can either delete a list, a single task, or wipe out the entire database
import sqlite3


def delete():
    database = 'bonus_todos.sqlite'
    conn = sqlite3.connect(database)
    cur = conn.cursor()

    # In case the user wishes to wipe out everything
    wipe1 = 'DELETE FROM todos'
    wipe2 = 'DELETE FROM todo_lists'

    # In case the user wants to delete a list
    list = 'DELETE FROM todo_lists WHERE list_id = ?'
    list_todos = 'DELETE FROM todos WHERE list_id = ?'

    # In case the user wants to delete a specific task
    todo = 'DELETE FROM todos WHERE todo_id = ?'

    task = ''
    while not task:
        user = input('To delete a list of todos, type LIST\n'
                     'To delete a todo, type TODO\n'
                     'If you wish to delete all todos and lists,type WIPE\n'
                     'To quit, type Q:  ')
        if not user or not user.strip():
            print('Invalid entry, please try again.')
        elif user == 'Q':
            break
        else:
            task += user
            if task == 'WIPE':
                prompt = input('Are you sure you want to do this? (Y/N):  ')
                if prompt == 'Y':
                    cur.execute(wipe1)
                    cur.execute(wipe2)
                    print('Done! Everything has been purged!')
                if prompt == 'N':
                    break
            else:
                if task == 'TODO':
                    prompt = input('Todo ID:  ')
                    cur.execute(todo, (prompt,))
                    print('Done! :)')
                elif task == 'LIST':
                    prompt = input('List ID:  ')
                    cur.execute(list, (prompt,))
                    cur.execute(list_todos, (prompt,))
                    print('Done! :)')
                else:
                    print('Invalid entry')

            conn.commit()
            conn.close()





