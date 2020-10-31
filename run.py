#!/usr/bin/env python3

import os
import requests

#Data for the dict: name, weight(int), description, image_name.
files_path = '/home/bryan/Documents/text_files/'
text_files = os.listdir('/home/bryan/Documents/text_files/')
#List to iterate and assign the matching image
image_directory = os.listdir('/where the modified pictures are located/')
data_dict = {}
i = 0
for text in text_files:
    with open(files_path+text, 'r') as file:        
        content = file.readlines()        
        
        fruit_weight = int(content[1].split(' ')[0])
        data_dict['name'] = content[0]        
        data_dict['weight'] = fruit_weight
        data_dict['description'] = content[2]
        data_dict['image_name'] = image_directory[i] 
        i += 1
    
        

