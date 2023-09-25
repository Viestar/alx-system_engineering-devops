#!/usr/bin/python3
""" Uses REST API to return information about an Employee """

import json
import requests


def employee_todo_progress():
    """ Dumps employee details """
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todo_all = {}

    for user in users:
        track_list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                dict_task = {"username": user.get('username'),
                             "task": task.get('title'),
                             "completed": task.get('completed')}
                track_list.append(dict_task)
        todo_all[user.get('id')] = track_list

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(todo_all, file)


if __name__ == "__main__":
    employee_todo_progress()
