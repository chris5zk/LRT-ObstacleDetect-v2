# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 18:49:35 2022

@author: chrischris
"""

import os
import cv2
import matplotlib.pyplot as plt
from pycocotools.coco import COCO

img = 'images'
lab = 'labels'
target = 'val'
annFile = f'{img}/{target}/_annotations.coco.json'
L_file = f'{lab}/{target}_labels'

coco = COCO(annFile)

try:
    os.makedirs(L_file)
except FileExistsError:
    pass

name = []


for file in os.listdir(f'{img}/{target}'):
    if file.endswith(".jpg"):
        name.append(file)
        
with open(f'{target}.lst', 'w') as f:
    for i in range(0,len(name)):
        print(i)
        annIds = coco.getAnnIds(imgIds = i)
        if annIds:
            anns = coco.loadAnns(annIds)
            Imgs = coco.loadImgs(anns[0]['image_id'])[0]['file_name']
            mask = coco.annToMask(anns[0])
            f.write(f'{img}/{target}/{Imgs} {L_file}/L_{Imgs}\n')
            cv2.imwrite(f'{L_file}/L_{Imgs}', mask*128)