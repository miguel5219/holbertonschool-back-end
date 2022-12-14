#!/usr/bin/python3
""" This module containts an api request """


if __name__ == "__main__":

    import csv
    import requests
    from sys import argv

    url_todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(argv[1])).json()
    url_user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()

    task_done_list = []
    with open('{}.json'.format(argv[1]), 'w') as f:
        for todo in url_todos:
            task_done_list.append({"task": todo['title'],
                                  "completed": todo['completed'],
                                   "username": url_user['username']})
        f.write(json.dumps({url_user['id']: task_done_list}))
