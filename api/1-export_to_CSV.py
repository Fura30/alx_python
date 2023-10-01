
import csv
import requests
import sys

if len(sys.argv) != 2:
  print("Usage: python3 export_to_CSV.py USER_ID")
  sys.exit(1)

user_id = sys.argv[1]

response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
if response.ok:
  user = response.json()
else:
  print(f"Error: could not retrieve information for user {user_id}")
  sys.exit(1)

response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/todos")
if response.ok:
  todos = response.json()
else:
  print(f"Error: could not retrieve tasks for user {user_id}")
  sys.exit(1)

filename = f"{user_id}.csv"

with open(filename, "w", newline="") as csvfile:
  writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
  writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
  for todo in todos:
    completed = "True" if todo["completed"] else "False"
    writer.writerow([user["id"], user["username"], completed, todo["title"]])

#print(f"Exported {len(todos)} tasks for user {user['username']} to {filename}")


