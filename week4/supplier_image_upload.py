#!/usr/bin/env python3

import requests
import os

user = os.getenv('USER')
path = '/home/'+user+'/supplier-data/images'

url = "http://localhost/upload/"

files = os.listdir(path)
for file in files:
    if '.jpeg' in file:
        opened = open(os.path.join(path, file), 'rb')
        r = requests.post(url, files={'file': opened})
