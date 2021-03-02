#!/usr/bin/env python3

import os
from PIL import Image
user = os.getenv('USER')
path = '/home/' + user + '/supplier-data/images'

files = os.listdir(path)
for file in files:
    if '.tiff' in file:
        image = Image.open(os.path.join(path, file)).convert('RGB').resize((600, 400))
        image.save(os.path.splitext(os.path.join(path, file))[0]+'.jpeg')
