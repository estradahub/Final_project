#!/usr/bin/env python3

from PIL import Image
import os

save_path = '/home/bryan/Documents/'
pic_directory = '/home/bryan/Pictures/'
images = os.listdir('/home/bryan/Pictures/')

for image in images:        
    im_name = os.path.basename(image).split('.')[0]      
    image = Image.open(pic_directory+image)
    resized = image.resize((600,400)).convert('RGB')
    resized.save(save_path+im_name, "JPEG")
    
