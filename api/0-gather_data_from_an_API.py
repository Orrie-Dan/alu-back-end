#!/usr/bin/python3
import requests

USERS_URL = "https://jsonplaceholder.typicode.com/users/"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos/"


def extract_data(employee_id):

import requests

USERS_URL = "https://jsonplaceholder.typicode.com/users/"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos/"


def extract_data(employee_id):
    
"""
    Function to extract and display information about an employee's completed tasks.
 Args:
        employee_id (int): The ID of the employee whose data you want to fetch.
    
    Process:
        - Makes an HTTP request to the USERS_URL endpoint to fetch the employee's details.
        - Makes an HTTP request to the TODOS_URL endpoint to get the list of todo items for the employee.
        - Iterates through the employee's todos and counts how many are marked as 'completed'.
    
    Returns:
        None: This function prints the result to the console. It doesn't return anything.
      
 """
    employee = requests.get(f"{USERS_URL}/{employee_id}").json()
    employee_name = employee["name"]
    employee_todos = requests.get(f"{TODOS_URL}?userId={employee_id}").json()
    completed_tasks = 0
    for todo in employee_todos:
        if todo["completed"]:
            completed_tasks += 1
print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{len(employee_todos)})")
    

extract_data(1)

