import csv
import requests
import sys

def fetch_employee_data(employee_id):
    # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    # Fetch employee data
    response_employee = requests.get(employee_url)
    employee_data = response_employee.json()
    employee_name = employee_data.get("name")

    # Fetch TODO list data
    response_todo = requests.get(todo_url)
    todo_list = response_todo.json()

    return employee_name, todo_list

def export_to_csv(employee_id, employee_name, todo_list):
    # Define the CSV filename
    csv_filename = f"{employee_id}.csv"

    # Write data to the CSV file
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_list:
            csv_writer.writerow([employee_id, employee_name, str(task["completed"]), task["title"]])

    print(f"Data has been exported to {csv_filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_name, todo_list = fetch_employee_data(employee_id)

    # Export data to CSV
    export_to_csv(employee_id, employee_name, todo_list)

if __name__ == "__main__":
    main()
 
