#!/usr/bin/python3
""" Uses REST API to return information about an Employee """


import json
import requests
import sys


def employee_todo_progress():
    """ Exports emplooyee data to a json """
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    user_todo = {}
    list_task = []

    for task in todos:
        if task.get('userId') == int(userId):
            dict_list = {"task": task.get('title'),
                         "completed": task.get('completed'),
                         "username": user.json().get('username')}
            list_task.append(dict_list)
    user_todo[userId] = list_task

    filename = userId + '.json'
    with open(filename, mode='w') as file:
        json.dump(user_todo, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    employee_todo_progress()
