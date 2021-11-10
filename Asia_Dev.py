# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 17:25:15 2021

@author: Admin
"""

import numpy as np
import os 

import argparse
import cv2

import sys

txt_1 = np.array([1,2,3,4,5,6])

#np.savetxt('testing_file.txt', txt_1, delimiter=',')


def videoCapture():
  save_path = '/home/mendel/AsiaM'
  file_name = 'output.mp4'
  
  completeName = os.path.join(save_path, file_name)

  parser = argparse.ArgumentParser()
  parser.add_argument('--camera_idx', type=int, help='Index of which video source to use. ', default = 0)
  args = parser.parse_args()

  args.camera_idx
  cap = cv2.VideoCapture(args.camera_idx)

  # Define the codec and create VideoWriter object
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  out = cv2.VideoWriter(completeName, fourcc, 20.0, (640,480))

  while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
      break
    
    cv2_im = frame

    cv2_im_rgb = cv2.cvtColor(cv2_im, cv2.COLOR_BGR2RGB)
    cv2_im_rgb = cv2.resize(cv2_im_rgb, (640,480))

    # output the frame
    out.write(cv2_im_rgb) 

    cv2.imshow('frame', cv2_im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()

  # After we release our webcam, we also release the output
  out.release() 

  cv2.destroyAllWindows()



def txt_saving():
    user_input = input('Your number?')
    if int(user_input) == 1:
        save_path = '/home/mendel/mnt/sdcard'
        file_name = 'testing_file.txt'
        
        completeName = os.path.join(save_path, file_name)
        print(completeName)
        
        f1 = open(completeName, "w+")
        f1.write("file information")
        f1.close()
        
    elif int(user_input) == 2:
        f1 = open('testing_here.txt', 'w+')
        f1.write("file here")
        f1.close()
        print("done")
        
    elif int(user_input) == 3:
        save_path = '/home/mnt'
        file_name = 'test_here.txt'
        
        completeName = os.path.join(save_path, file_name)
        print(completeName)
        
        f1 = open(completeName, "w+")
        f1.write("file information")
        f1.close()
        
    elif int(user_input) == 4:
        save_path = '/home/mendel/AsiaM'
        file_name = 'test_here.txt'
        
        completeName = os.path.join(save_path, file_name)
        print(completeName)
        
        f1 = open(completeName, "w+")
        f1.write("file information")
        f1.close()

if __name__ == '__main__':
    videoCapture()