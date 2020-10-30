#!/usr/bin/env python3

import os
import requests

#Data for the dict: name, weight(int), description, image_name.
files_path = '/home/bryan/Documents/text_files/'
text_files = os.listdir('/home/bryan/Documents/text_files/')
data_dict = {}
for text in text_files:
    with open(files_path+text, 'r') as file:
        content = file.readlines()
        fruit_weight = int(content[1].split(' ')[0])
        data_dict['name'] = content[0]        
        data_dict['weight'] = fruit_weight
        data_dict['description'] = content[2]
        data_dict['image_name'] = "Working on it"
    print(data_dict)
        

