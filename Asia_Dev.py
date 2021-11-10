# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 17:25:15 2021

@author: Admin
"""

import numpy as np
import os 

import sys

txt_1 = np.array([1,2,3,4,5,6])

#np.savetxt('testing_file.txt', txt_1, delimiter=',')
user_input = input('Your number?')

if int(user_input) == 1:
    save_path = 'home/mendel/mnt/sdcard'
    file_name = 'testing_file.txt'
    
    completeName = os.path.join(save_path, file_name)
    print(completeName)
    
    f1 = open(completeName, "w")
    f1.write("file information")
    f1.close()
    
elif int(user_input) == 2:
    f1 = open('testing_here.txt', 'w')
    f1.write("file here")
    f1.close()
    print("done")
    
elif int(user_input) == 3:
    save_path = 'home/mendel/mnt'
    file_name = 'test_here.txt'
    
    completeName = os.path.join(save_path, file_name)
    print(completeName)
    
    f1 = open(completeName, "w")
    f1.write("file information")
    f1.close()