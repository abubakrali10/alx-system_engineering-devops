#!/usr/bin/python3
"""export data in the CSV format from an API"""
import requests
import sys


if __name__ == '__main__':
    u_id = sys.argv[1]
    payload = {'userId': u_id}
    api_url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(f"{api_url}/users/{u_id}").json()
    todos = requests.get(f"{api_url}/todos", params=payload).json()
    completed = [todo["title"] for todo in todos if todo["completed"]]

    csv_file_path = f"{u_id}.csv"
    with open(csv_file_path, mode='w') as csv_file:
        for task in todos:
            csv_file.write('"{}","{}","{}","{}"\n'
                           .format(u_id, user["username"],
                                   task["completed"], task["title"]))
