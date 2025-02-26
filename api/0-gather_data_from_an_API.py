#!/usr/bin/python3
import requests

USERS_URL = "https://jsonplaceholder.typicode.com/users/"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos/"


def extract_data(employee_id):
    employee = requests.get(f"{USERS_URL}/{employee_id}").json()
    employee_name = employee["name"]
    employee_todos = requests.get(f"{TODOS_URL}?userId={employee_id}").json()
    completed_tasks = 0
    for todo in employee_todos:
        if todo["completed"]:
            completed_tasks += 1
print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{len(employee_todos)})")
    

extract_data(1)

