#!/usr/bin/python3
"""exports data in the JSON format from an API"""
import requests
import sys
import json


if __name__ == '__main__':
    u_id = sys.argv[1]
    payload = {'userId': u_id}
    api_url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(f"{api_url}/users/{u_id}").json()
    todos = requests.get(f"{api_url}/todos", params=payload).json()
    completed = [todo["title"] for todo in todos if todo["completed"]]

    json_file_path = f"{u_id}.json"
    with open(json_file_path, mode='w') as json_file:
        json.dump({u_id: [{
            "task": task["title"],
            "completed": task["completed"],
            "username": user["username"],
        } for task in todos]}, json_file)
