#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if len(sys.argv) != 2:
    print("Please provide an employee ID as a parameter.")
    exit()

employee_id = sys.argv[1]

try:
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_response.raise_for_status()
    user = user_response.json()

    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todos_response.raise_for_status()
    todos = todos_response.json()

    completed_tasks = [task['title'] for task in todos if task['completed']]
    total_tasks = len(todos)

    print(f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")

except requests.exceptions.HTTPError as e:
    print(f"Error: {e}")
