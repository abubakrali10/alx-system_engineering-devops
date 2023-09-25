#!/usr/bin/python3
"""Gathering todo list from an API using Employee ID"""
import requests
import sys


if __name__ == '__main__':
    u_id = sys.argv[1]
    payload = {'userId': u_id}
    api_url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(f"{api_url}/users/{u_id}").json()
    todos = requests.get(f"{api_url}/todos", params=payload).json()
    completed = [todo["title"] for todo in todos if todo["completed"]]
    c_len = len(completed)
    t_len = len(todos)
    print(f"Employee {user['name']} is done with tasks({c_len}/{t_len}):")
    [print(f"\t {c}") for c in completed]
