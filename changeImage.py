#!/usr/bin/env python3

from PIL import Image
import os

save_path = '/home/bryan/Documents/'
imagen = Image.open('/home/bryan/Pictures/error.png')
resized = imagen.resize((600,400)).convert('RGB')
#To capture the name of the file and save it with the same name other format
for image in images:        
    im_name = os.path.basename(image).split('.')  
resized.save(save_path+'test.jpg', "JPEG")

print(resized) 