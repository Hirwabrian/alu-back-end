#!/usr/bin/python3
"""
This script fetches the TODO list progress for a given employee ID from a
REST API and exports the tasks data to a JSON file.
"""


import json
import requests
import sys


def get_employee_todo_progress(id):
    Name = f"https://jsonplaceholder.typicode.com/users/{id}"
    todos = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    
    user_response = requests.get(Name)
    if user_response.status_code != 200:
        print("Error fetching user data")
        return
    # Fetch user name
    user_data = user_response.json()
    username = user_data.get('username')

    # Fetch todo list 
    todos_response = requests.get(todos)
    if todos_response.status_code != 200:
        print("Error fetching TODO data")
        return
    
    todos_data = todos_response.json()

    # Prepare data for JSON export
    tasks_list = [
        {"task": task.get('title'), "completed": task.get('completed'), "username": username}
        for task in todos_data
    ]
    data = {str(id): tasks_list}

    # Export data to JSON file
    json_filename = f"{id}.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(data, json_file, indent=4)


    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    try:
        id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    
    get_employee_todo_progress(id)
