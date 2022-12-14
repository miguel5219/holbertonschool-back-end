#!/usr/bin/python3
""" This module containts an api request """


if __name__ == "__main__":

    import json
    import requests


    url_todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos").json()
    url_user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}").json()

    dictionary = {}
    for user in url_user:
        username = ['username']
        list_task = []
        for task in todos:
            if task['userId'] == user['id']:
                dictionary_1 = {}
                dictionary_1['username'] = username
                dictionary_1['task'] = task['title']
                dictionary_1['completed'] = task['completed']
                list_task.append(dictionary_1)
        dictionary[user['id']] = list_task

    with open("todo_all_employees.json", 'w') as f:
        json.dump(dictionary, f)
