#! /usr/bin/env python3

import os
import requests
import json

user = os.getenv('USER')
path = '/home/'+user+'/supplier-data/descriptions'
image_path = '/home/'+user+'/supplier-data/images'
url = 'http://localhost/fruits/'

files = os.listdir(path)
for file in files:
    f = open(os.path.join(path, file), 'r')
    fruits_data = {}
    name = ''
    weight = ''
    description = ''
    i=0
    for line in f:
        if i==0:
            name = line
        if i==1:
            weight = int(line.split()[0])
        if i>=2:
            description += line
        i+=1
    fruits_data['name'] = name.strip('\n')
    fruits_data['weight'] = weight
    fruits_data['description'] = description.strip('\n')
    fruits_data['image_name'] = os.path.splitext(file)[0] +'.jpeg'
    print(fruits_data)

    # sending requests
    r = requests.post(url, json=fruits_data)
    # print(r)
