import requests
import json

req = requests.get\
    ("https://jsonplaceholder.typicode.com/users")
print(f'HTTP Status code: {req.status_code}')
print(f'HTTP Header: {req.headers}')
json_r = json.loads(req.content)
print(json_r)

class User:
    def __init__(self, jsonObj):
        self.__dict__ = jsonObj
    def __rep__(self):
        res = ''
        for k,v in\
                self.__dict__.items():
            res += f'{k} : {v} '
        return res

#u = User(json_r)
#print(u.name)
#rint(u.id)

# GET - brings data (all)
# GET / id - brings specific id
# POST - add
# PUT - update
# DELETE

data = {'title' : 'Python request',
        'body' : 'My request body',
        'userId' : 1}
result = requests.post("https://jsonplaceholder.typicode.com/users",
              data)
print(result.status_code)
print(result.text)

result = requests.put("https://jsonplaceholder.typicode.com/users/1",
              data)
print(result.status_code)
print(result.text)

result = requests.delete("https://jsonplaceholder.typicode.com/users/1")
print(result.status_code)
print(result.text)
