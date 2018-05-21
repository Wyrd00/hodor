#!/usr/bin/python3

import requests

url = "http://158.69.76.135/level0.php"
p = {"id": "346", "holdthedoor": "Submit"}

for i in range(1024):
    r = requests.post(url, p)
print(r.content)
