#!/usr/bin/python3
# Import the requests module to make HTTP requests.
import requests

# Define URLs for the placeholder API to get user data and todo items.
USERS_URL = "https://jsonplaceholder.typicode.com/users/"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos/"

def extract_data(employee_id):
    """
    Function to extract and display information about an employee's completed tasks.
    
    This function retrieves an employee's data (name) and their todo items 
    using their unique employee_id, then counts how many tasks the employee 
    has completed, and displays a formatted message with the results.
    
    Args:
        employee_id (int): The ID of the employee whose data you want to fetch.
    
    Process:
        - Makes an HTTP request to the USERS_URL endpoint to fetch the employee's details.
        - Makes an HTTP request to the TODOS_URL endpoint to get the list of todo items for the employee.
        - Iterates through the employee's todos and counts how many are marked as 'completed'.
    
    Returns:
        None: This function prints the result to the console. It doesn't return anything.
    
    Example:
        extract_data(1)
        # Output: Employee Leanne Graham is done with tasks (5/10)
    """
    
    # Fetch employee data (name) from the API based on the employee_id.
    employee = requests.get("{}{}".format(USERS_URL,employee_id)).json()  # Make GET request to fetch employee details.
    employee_name = employee["name"]  # Extract the employee's name from the response JSON.

    # Fetch the list of todos associated with the employee using their employee_id.
    employee_todos = requests.get("{}?userId={}".format(TODOS_URL, employee_id)).json()  # Make GET request for todos.

    # Initialize a variable to count the completed tasks.
    completed_tasks = 0
    
    # Loop over the todos and count the ones marked as 'completed'.
    for todo in employee_todos:
        if todo["completed"]:  # Check if the current todo is marked as completed.
            completed_tasks += 1  # Increment the count of completed tasks.

    # Print a message summarizing the number of completed tasks vs total tasks.
    print("Employee {} is done with tasks ({}/{})".format(employee_name, completed_tasks, len(employee_todos)))

# Call the function with employee ID 1 to extract and display the data.
extract_data(1)

