import sys
import requests

def get_employee_info(employee_id):
    """
    Retrieves employee information and displays their TODO list progress.

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

    # Calculate TODO list progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for todo in todo_data if todo['completed'])

    # Display TODO list progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for todo in todo_data:
        if todo['completed']:
            print("\t", todo['title'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
