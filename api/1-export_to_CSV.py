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
 # Fetch employee details
    response = requests.get(f"{USERS_URL}/{employee_id}")
    if response.status_code != 200:
        print("Error: Unable to fetch employee data.")
        return
    
    employee = response.json()
    username = employee.get("username", "Unknown")
    
    # Fetch employee's tasks
    response = requests.get(f"{TODOS_URL}?userId={employee_id}")
    if response.status_code != 200:
        print("Error: Unable to fetch tasks.")
        return
    
    employee_todos = response.json()
    
    # CSV file name based on employee ID
    filename = f"{employee_id}.csv"
    
    # Write data to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        
        # Write header row
        writer.writerow(["Employee ID", "Username", "Completed", "Task Title"])
        
        # Write each task as a row in the CSV file
        for todo in employee_todos:
            writer.writerow([
                employee_id,
                username,
                todo.get("completed", False),
                todo.get("title", "No Title")
            ])
    
    print(f"Data successfully exported to {filename}")

# Example usage
if __name__ == "__main__":
    extract_and_export_to_csv(1)

