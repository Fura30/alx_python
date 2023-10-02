
import csv
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    # Get employee details
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

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
        # Get employee details

    csv_filename = "{}.csv".format(employee_id)

    with open(csv_filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
      #  csvwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csvwriter.writerows(employee_tasks)
