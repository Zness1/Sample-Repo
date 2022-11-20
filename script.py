"""Module Docstring Before Stage"""
import sys
import requests

def greet(who_to_greet):
    """Function Docstring"""
    greeting = f'Hello, {who_to_greet}'
    return greeting

r = requests.get(url='https://coreyms.com', timeout=(2, 4))

print(greet('Zeeman'))
print(sys.executable)
print(r.status_code)
r.close()
