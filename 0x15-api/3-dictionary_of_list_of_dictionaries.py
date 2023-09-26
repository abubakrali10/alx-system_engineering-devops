#!/usr/bin/python3
"""exports all data in the JSON format from an API"""
import json
import requests


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(f"{api_url}/users").json()

    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump({user['id']: [{
            "task": task["title"],
            "completed": task["completed"],
            "username": user["username"],
        } for task in requests.get(f"{api_url}/todos",
                                   params={"userId": user["id"]}).json()]
          for user in users}, json_file)
