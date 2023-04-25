#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if len(sys.argv) != 2:
    print("Please provide an employee ID as a parameter.")
    exit()

employee_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/"

try:
    # Fetch user information
    user_response = requests.get(f"{url}users/{employee_id}")
    user_response.raise_for_status()
    user = user_response.json()
    username = user.get("username")

    # Fetch todos for the employee
    todos_response = requests.get(f"{url}todos", params={"userId": employee_id})
    todos_response.raise_for_status()
    todos = todos_response.json()

    # Write todos to CSV file
    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([employee_id, username, todo.get("completed"), todo.get("title")])

    print(f"Todo list for employee {username} exported to {employee_id}.csv")

except requests.exceptions.HTTPError as e:
    print(f"Error: {e}")
