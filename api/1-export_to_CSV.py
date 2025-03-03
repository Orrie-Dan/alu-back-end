#!/usr/bin/python3
"""
Module: extract_employee_todos

Description:
This module fetches employee details and their corresponding to-do list tasks from
a mock API (JSONPlaceholder) and exports the data to a CSV file. Each task entry
includes the employee ID, username, task completion status, and task title.
"""
import requests
import csv

# API endpoints
USERS_URL = "https://jsonplaceholder.typicode.com/users/"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos/"


def extract_and_export_to_csv(employee_id):
    # Fetch employee details
    employee = requests.get(f"{USERS_URL}/{employee_id}").json()
    username = employee["username"]

    # Fetch employee's tasks
    employee_todos = requests.get(f"{TODOS_URL}?userId={employee_id}").json()

    # CSV file name
    filename = f"{employee_id}.csv"

    # Write to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Write each task as a row
        for todo in employee_todos:
            writer.writerow([employee_id, username, todo["completed"], todo["title"]])

    print(f"Data successfully exported to {filename}")


# Example usage
extract_and_export_to_csv(1)

