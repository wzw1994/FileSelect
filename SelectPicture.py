# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 11:49:15 2018

@author: Baymax_58
@For getting image information to ease the mission of selecting picture 
"""

import os
import shutil
from PIL import Image

OriDirPath = "./Picture_Origin"
RemainDirPath = "./Picture_Remain"
RejectDirPath = "./Picture_Reject"

for Dirname in os.listdir(OriDirPath):
    DirPath = OriDirPath + '/' + Dirname
    for Filename in os.listdir(DirPath):
        FilePath = DirPath + '/' + Filename
        img = Image.open(FilePath)
        imgsize = img.size
        if (imgsize[0] < 200 or imgsize[1] < 200):
            TowardsDirPath =  RejectDirPath + '/' + Dirname
            if not os.path.exists(TowardsDirPath):
                os.makedirs(TowardsDirPath)
            TowardsFilePath = TowardsDirPath + '/' + Filename
            shutil.copyfile(FilePath,TowardsFilePath)
        else:
            TowardsDirPath = RemainDirPath + '/' + Dirname
            if not os.path.exists(TowardsDirPath):
                os.makedirs(TowardsDirPath)
            TowardsFilePath = TowardsDirPath + '/' + Filename
            shutil.copyfile(FilePath,TowardsFilePath)


