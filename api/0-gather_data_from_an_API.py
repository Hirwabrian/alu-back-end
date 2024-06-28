"""
This script fetches the TODO list progress for a given employee ID from a REST API.
It displays the employee's name, the number of completed tasks, the total number of tasks,
and the titles of the completed tasks.

Usage:
    python script.py <employee_id>

Requirements:
    - The script accepts an integer as a parameter, which is the employee ID.
    - The script displays the employee's TODO list progress in the specified format.
    - Uses the requests module to interact with the REST API.

Example:
    python script.py 1

Output Format:
    First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    Subsequent lines: Titles of completed tasks with one tabulation and one space before each title.
"""

import sys
import requests

def get_employee_todo_progress(employee_id):
    # Base URLs for the API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    
    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error fetching user data")
        return
    
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todo list data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error fetching TODO data")
        return
    
    todos_data = todos_response.json()

    # Calculate completed and total tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print the first line of output
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")

    # Print the titles of completed tasks
    for index, task in enumerate(done_tasks, start=1):
        print(f"\t{index}. {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)
