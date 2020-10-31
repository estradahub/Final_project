#!/usr/bin/env python3
import requests
import os

#How to upload files to a webserver using the request module (simple way

images_directory = '/where the images are located/'
images = os.listdir(images_directory

url = "http://localhost/upload/"
      
for image in images:      
    with open(images_directory+image, 'rb') as opened:     
        r = request.post(url, files={'file': opened})