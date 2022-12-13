#!/usr/bin/python3
""" This module containts an api request """

if __name__ == "__main__":

    import requests
    from sys import argv

    url_todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1]))
    url_user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))

    task_complete = 0
    all_tasks = 0
    list_task_complete = []

    for task in url_todos.json():
        all_tasks += 1
        if task['completed'] is True:
            task_complete += 1
            list_task_complete.append(task['title'])

    employee_name = url_user.json()['name']
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, task_complete, all_tasks))

    for task in list_task_complete:
        print("\t {}".format(task))
