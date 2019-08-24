import requests # need to install in settings
import json

req = requests.get("https://jsonplaceholder.typicode.com/todos")
print(req.status_code)
