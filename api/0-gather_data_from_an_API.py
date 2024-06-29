#!/usr/bin/python3
"""
This script fetches the TODO list progress for a given employee ID from a
REST API.
"""

import requests
import sys


def get_employee_todo_progress(id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"

    user_response = requests.get(user_url)
    user_response.raise_for_status()  # Ensure we handle HTTP errors

    # Fetch user name
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todo list
    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()  # Ensure we handle HTTP errors

    todos_data = todos_response.json()

    # Calculate completed and total tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print the first line of output
    print(f"Employee {employee_name} is done with tasks("
          f"{number_of_done_tasks}/{total_tasks}):")

    # Print the titles of completed tasks
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(id)
