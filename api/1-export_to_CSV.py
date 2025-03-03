#!/usr/bin/python3
"""
Module: extract_employee_todos

Description:
This module fetches employee details and their corresponding to-do list tasks from
a mock API (JSONPlaceholder) and exports the data to a CSV file. Each task entry
includes the employee ID, username, task completion status, and task title.
"""
import csv
import requests

# API endpoints
USERS_URL = "https://jsonplaceholder.typicode.com/users/"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos/"
def extract_and_export_to_csv(employee_id):
    try:
        employee = requests.get(f"{USERS_URL}{employee_id}").json()
        tasks = requests.get(f"{TODOS_URL}?userId={employee_id}").json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return
    
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows([[employee_id, employee["username"], task["completed"], task["title"]] for task in tasks])
    
    print(f"Data successfully exported to {filename}")

# Example usage
extract_and_export_to_csv(1)
extract_and_export_to_csv(2)


