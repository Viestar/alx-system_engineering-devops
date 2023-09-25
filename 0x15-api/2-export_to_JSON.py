#!/usr/bin/python3
""" Uses REST API to return information about an Employee """


import json
import requests
import sys


def employee_todo_progress(emp_id):
    """ Exports emplooyee data to a json """
    userId = emp_id
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todoUser = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
    todoUser[userId] = taskList

    filename = userId + '.json'
    with open(filename, mode='w') as file:
        json.dump(todoUser, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    emp_id = (sys.argv[1])
    employee_todo_progress(int(emp_id))
