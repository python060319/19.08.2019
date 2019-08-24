import requests # need to install in settings
import json

class Todos:
    def __init__(self, d):
        self.__dict__ = d
    def __repr__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += ' '
        return result + " || "
    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += '\n'
        return result

# solution 1:
list_Todos = [ ]
for n in range(1, 10):
    resp = requests.get(f'https://jsonplaceholder.typicode.com/todos/{n}')
    d = json.loads(resp.content)
    item = Todos(d)
    list_Todos.append(item)

print(list_Todos)

# solution 2 (much better):
resp = requests.get(f'https://jsonplaceholder.typicode.com/todos')
d_list = json.loads(resp.content)
list_Todos = [ ]
for d in d_list:
    item = Todos(d)
    list_Todos.append(item)

print(list_Todos)
