
import csv
import requests
from sys import argv


def export_to_csv(employee_id):
    """
    Export the tasks owned by the employee with the given ID to a CSV file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    employee_response = requests.get(user_url)
    tasks_response = requests.get(tasks_url)

    employee_data = employee_response.json()
    tasks_data = tasks_response.json()

    employee_name = employee_data.get("username")
    employee_tasks = []

    for task in tasks_data:
        task_completed = task.get("completed")
        task_title = task.get("title")
        employee_tasks.append([employee_id, employee_name, str(task_completed), task_title])

    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csvwriter.writerows(employee_tasks)


if __name__ == "__main__":
    employee_id = int(argv[1])
    export_to_csv(employee_id)
