#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

import json
from requests import get
from sys import argv

if __name__ == "__main__":
    todos_response = get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = todos_response.json()

    user_row = []
    users_response = get('https://jsonplaceholder.typicode.com/users')
    users_data = users_response.json()

    for user_data in users_data:
        if user_data['id'] == int(argv[1]):
            username = user_data['username']
            user_id = user_data['id']

    user_row = []

    for todo_data in todos_data:

        todo_dict = {}

        if todo_data['userId'] == int(argv[1]):
            todo_dict['username'] = username
            todo_dict['task'] = todo_data['title']
            todo_dict['completed'] = todo_data['completed']
            user_row.append(todo_dict)

    final_user_dict = {}
    final_user_dict[user_id] = user_row
    json_object = json.dumps(final_user_dict)

    with open(argv[1] + ".json",  "w") as json_file:
        json_file.write(json_object)
