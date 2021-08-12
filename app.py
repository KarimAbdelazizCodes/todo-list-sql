from create_todo_list import new_list
from new_todo import new_todo
from current_lists import show_current_lists
from list_todos import list_todos
from search_todos import find_todo
from delete_todo_or_list import delete


class Todos:
    running = True

    def __init__(self, name):
        self.name = name
        self.initiate()

    def initiate(self):
        print(f'Hello, {self.name}!'
              f'\nTo create a new todo list, type NEW LIST'
              f'\nTo view current lists, type VIEW'
              f'\nTo view todos, type TODOS'
              f'\nTo add a new todo, type NEW TODO'
              f'\nTo search todos, type FIND'
              f'\nTo delete items, type DEL'
              f'\nTo terminate the program, type DONE')
        while self.running:
            user_input = input('What would you like to do?  ')
            if user_input == 'DONE':
                self.running = not self.running
                print('Keep \'em coming! See you soon!')
            elif user_input == 'NEW LIST':
                self.new_list()
            elif user_input == 'VIEW':
                self.all_lists()
            elif user_input == 'TODOS':
                self.show_todos()
            elif user_input == 'NEW TODO':
                self.new_todo()
            elif user_input == 'FIND':
                self.find_todo()
            elif user_input == 'DEL':
                self.delete()
            else:
                print('Please make sure you\'ve entered a valid command.')

    def new_list(self):
        new_list()

    def new_todo(self):
        new_todo()

    def all_lists(self):
        show_current_lists()

    def show_todos(self):
        list_todos()

    def find_todo(self):
        find_todo()

    def delete(self):
        delete()



karim = Todos('Karim')

