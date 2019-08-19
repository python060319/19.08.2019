import requests
import json

req = requests.get\
    ("https://jsonplaceholder.typicode.com/users/1")
print(f'HTTP Status code: {req.status_code}')
print(f'HTTP Header: {req.headers}')
json_r = json.loads(req.content)
print(json_r)

class User:
    def __init__(self, jsonObj):
        self.__dict__ = jsonObj
    def __str__(self):
        pass

u = User(json_r)
print(u.name)
print(u.id)

# read all users with get
# create objects for all of the users, create a list from all of  the users
# implement __str__
# print the list
