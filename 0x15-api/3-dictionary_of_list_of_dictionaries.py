#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

import json
from requests import get

if __name__ == "__main__":
    todos_response = get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = todos_response.json()

    users_response = get('https://jsonplaceholder.typicode.com/users')
    users_data = users_response.json()

    all_users_todos = {}

    for user in users_data:
        user_todos = []

        for todo in todos_data:
            if user['id'] == todo['userId']:
                todo_entry = {
                    'username': user['username'],
                    'task': todo['title'],
                    'completed': todo['completed']
                }
                user_todos.append(todo_entry)

        all_users_todos[user['id']] = user_todos

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_users_todos, json_file, indent=2)
