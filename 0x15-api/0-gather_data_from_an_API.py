#!/usr/bin/python3
"""
     a Python script that, uses a REST API, for a given employee ID,
     returns information about his/her TODO list progress.
"""

import requests
from sys import argv


def scrape(id):
    """Scrape data from REST API"""
    user_name = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}",).json()["name"]

    todo_data = requests.get(
        f"https://jsonplaceholder.typicode.com/todos",).json()

    total, completed = 0, 0
    todos = []

    for data in todo_data:
        if data["userId"] == id:
            total += 1

            if data["completed"]:
                completed += 1
                todos.append(data["title"])

    print("Employee {} is done with tasks({}/{}):".format(
                                    user_name, completed, total))

    for todo in todos:
        print("\t {}".format(todo))


if __name__ == "__main__":
    id = int(argv[1])
    scrape(id)
