"""Module Docstring GitHub"""
import sys
import requests
import generators_demo

def greet(who_to_greet):
    """Function Docstring"""
    greeting = f'Hello, {who_to_greet}'
    return greeting

r = requests.get(url='https://coreyms.com', timeout=(2, 4))

print(greet('Zeeman'))
print(sys.executable)
print(r.status_code)
r.close()

print(generators_demo.__doc__)
