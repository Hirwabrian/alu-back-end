#!/usr/bin/python3
"""
This script fetches the TODO list progress for all employees from a
REST API and exports the tasks data to a JSON file.
"""

import json
import requests


def main():
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"

    # Fetch all user data
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Fetch todo list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare data for JSON export
    all_tasks = {}
    for user in users_data:
        user_id = str(user['id'])
        username = user['username']
        user_tasks = [
            task for task in todos_data if task['userId'] == user['id']]
        task_list = [{'username': username, 'task': task['title'],
                      'completed': task['completed']} for task in user_tasks]
        all_tasks[user_id] = task_list

    # Write the result to a JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    main()
