#!/usr/bin/python3
"""
This script fetches the TODO list progress for a given employee ID from a REST API and exports
 the data to a CSV file.
"""


import csv
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
    employee_name = user_data.get('name')
    username = user_data.get('username')


    # Fetch todo list 
    todos_response = requests.get(todos)
    if todos_response.status_code != 200:
        print("Error fetching TODO data")
        return
    
    todos_data = todos_response.json()
    # Export data to CSV
    csv_filename = f"{id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([id, username, task.get('completed'), task.get('title')])



if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    try:
        id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    
    get_employee_todo_progress(id)
