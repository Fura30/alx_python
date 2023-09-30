#!/usr/bin/python3
import csv
import requests
import sys


def get_employee_info(employee_id):
    """
    Retrieves employee information and exports their TODO list in CSV format.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data['name']

    # Get employee TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todo_data = response.json()

    # Export TODO list to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todo_data:
            writer.writerow([employee_id, employee_name, str(todo['completed']), todo['title']])

    print(f"TODO list exported to {filename}")

if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
