"""Docstring"""

import requests

r = requests.get("https://coreyms.com", timeout=(2,4))
print(r.status_code)
print(r.ok)
