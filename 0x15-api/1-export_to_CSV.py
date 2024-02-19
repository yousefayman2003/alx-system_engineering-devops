#!/usr/bin/python3
"""
     a Python script that, uses a REST API, for a given employee ID,
     returns information about his/her TODO list progress.
"""

import csv
import requests
from sys import argv


def scrape(id):
    """Scrape data from REST API"""
    user_name = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}",).json()["name"]

    todo_data = requests.get(
        f"https://jsonplaceholder.typicode.com/todos",).json()

    with open(f"{id}.csv", "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for data in todo_data:
            row = []
            if data["userId"] == id:
                row.append(id)
                row.append(user_name)
                row.append(data["completed"])
                row.append(data["title"])

                writer.writerow(row)


if __name__ == "__main__":
    id = int(argv[1])
    scrape(id)
