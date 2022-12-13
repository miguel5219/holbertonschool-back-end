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

    with open('{}.csv'.format(argv[1]), 'w', newline='') as f:
        the_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for todo in url_todos:
            the_writer.writerow([url_user['id'], url_user['username'],
                                todo['completed'], todo['title']])
