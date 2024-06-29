#!/usr/bin/python3
"""
This script fetches the TODO list progress for all employees from a
REST API and exports the tasks data to a JSON file.
"""

import json
import requests
import sys

def get_employee_todo_progress(id):
    todos = f"https://jsonplaceholder.typicode.com/todos?userId={id}"

    users_url = "https://jsonplaceholder.typicode.com/users"
    # Fetch all user data
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Fetch todo list 
    todos_response = requests.get(todos)
    todos_data = todos_response.json()

    # Prepare data for JSON export
    tasks_by_user = []
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')
        tasks = [
            {"username": username, "task": task.get('title'), "completed": task.get('completed')}
            for task in todos_data if task.get('userId') == user_id
        ]
        tasks_by_user[str(user_id)] = tasks
        

    # Write the result to a JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(tasks_by_user, json_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    try:
        id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    
    get_employee_todo_progress(id)
