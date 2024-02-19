#!/usr/bin/python3

"""Python script that gets data from REST API and saves it
in the CSV format"""

import csv
from requests import get
from sys import argv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = response.json()  # Renamed data to todos_data
    response2 = get('https://jsonplaceholder.typicode.com/users')
    users_data = response2.json()  # Renamed data2 to users_data

    for user in users_data:  # Changed variable name to user
        if user['id'] == int(argv[1]):
            employee = user['username']

    with open(argv[1] + '.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for todo in todos_data:  # Changed variable name to todo
            if todo['userId'] == int(argv[1]):
                row = [todo['userId'], employee, todo['completed']]
                row.append(todo['title'])
                writer.writerow(row)
