#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:56:31 2020

@author: arsh
"""
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import load_weights
import pandas as pd
import utils
from options import options
import os

def draw_boxes(detection_result,class_names,file_name):
    """ 
    image= image
    detection_result=dictionary of class to [box_cen_x,box_cen_y,box_width,box_height,confidence]
    class_names=array of class_names
    """
    source_img = Image.open(file_name)
    source_img=source_img.resize((416,416))
    for i in detection_result.keys():
        if(len(detection_result[i])==0):
            continue
        label=class_names[i]
        box_cen_x=detection_result[i][0][0]
        box_cen_y=detection_result[i][0][1]
        box_width=detection_result[i][0][2]
        box_height=detection_result[i][0][3]
        
        draw = ImageDraw.Draw(source_img)
        draw.rectangle(((box_cen_x,box_cen_y ), (box_height, box_width)))
        font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
        draw.text((box_cen_x, box_cen_y),label,font=font ,fill=(255,255,255,128) )
     
    source_img.save('results/'+file_name.split('/')[-1],'JPEG')

file_name="coco.names"
classes_names = utils.load_class_names('./data/labels/coco.names')

if(('results' in os.listdir(os.getcwd()))== False):
   os.mkdir('results')

options=options()()
data_path=options.data_path
#names of images
image_names=os.listdir(data_path)
# detecting objects in each image
for i in image_names:
    file=data_path+"/"+i
    detection_result=load_weights.main(file)
    #detection_result=detection_result[0]
    # draws boxes and saves the results in results folder
    utils.draw_boxes([file],detection_result,classes_names,(416,416))
    #draw_boxes(detection_result[0],classes_names,file)







 
