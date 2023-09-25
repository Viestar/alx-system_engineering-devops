#!/usr/bin/python3
""" Uses REST API to return information about an Employee """
import requests

import sys


def employee_todo_progress(emp_id):
    """ outputs employees to do list """
    api_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{api_url}/todos?userId={emp_id}"
    user_url = f"{api_url}/users/{emp_id}"
    try:
        # Fetching employee credentials
        user_response = requests.get(user_url)
        emp_details = user_response.json()
        emp_name = emp_details.get('name')

        # Fetching todo list
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()
        total_t = len(todo_list)
        comp_t = 0
        comp_tasks_list = []
        for task in todo_list:
            if task['completed']:
                comp_tasks_list.append(task)
                comp_t += 1

        # Formatting and printing the data to standard output
        print(f"Employee {emp_name} is done with tasks ({comp_t}/{total_t}):")
        for task in comp_tasks_list:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as int_error:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    emp_id = (sys.argv[1])
    employee_todo_progress(int(emp_id))
