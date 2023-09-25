#!/usr/bin/python3
""" Uses REST API to return information about an Employee """
import csv
import requests

import sys


def employee_todo_progress(emp_id):
    """ Saves employee details in a csv file """
    api_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{api_url}/todos?userId={emp_id}"
    user_url = f"{api_url}/users/{emp_id}"
    try:
        # Fetching employee credentials
        user_response = requests.get(user_url)
        emp_details = user_response.json()
        emp_name = emp_details.get('name')
        uid = sys.argv[1]

        # Fetching todo list
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()
        tasks_list = [task for task in todo_list]

        # Writing data to the csv file
        csv_filename = f"{uid}.csv"
        with open(csv_filename, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_ALL, lineterminator='\n')
            for task in tasks_list:
                csv_writer.writerow(
                    [uid, emp_name, str(task['completed']), task['title']])

    except requests.exceptions.RequestException as int_error:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    emp_id = (sys.argv[1])
    employee_todo_progress(int(emp_id))
