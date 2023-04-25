#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")
user = user_response.json()
todos_response = requests.get(
    f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}")
todos = todos_response.json()
completed_tasks = [task['title'] for task in todos if task['completed']]
print(
    f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{len(todos)}):")
for task in completed_tasks:
    print(f"\t{task}")
