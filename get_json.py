import requests # need to install in settings
import json

resp = requests.get\
    ("https://jsonplaceholder.typicode.com/todos/1")
print(f'Status code = {resp.status_code}')
#print(f'Header = {resp.headers}')
#print(resp.content)

d = json.loads(resp.content)
class Todos:
    def __init__(self, d):
        self.__dict__ = d
    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += '\n'
        return result

t = Todos(d)
print(t.userId)
