# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 17:25:15 2021

@author: Admin
"""

import numpy as np
import os 

import argparse
import cv2

from datetime import datetime, timedelta

import sys
#import keyboard


def videoCapture(t_now, video):
  print('recording')
  while video.cap.isOpened():
    ret, frame = video.cap.read()
    
    if not ret:
      print('welp')
      break
    
    cv2_im = frame
    # output the frame
    video.out.write(cv2_im) 

    if datetime.now().replace(microsecond=0) == (t_now + timedelta(seconds=10)):
      video.out.release()
      print('saved')

      t_now = datetime.now().replace(microsecond=0)
      file_name = 'output_' + t_now.strftime(t_format) + '.mp4'
      video.updatePath(file_name)
    
    # for displaying on the monitor
    #cv2.imshow('frame', cv2_im)
    #if keyboard.is_pressed('q'):
    #  print('terminate')
    #  break

  video.cap.release()

  # After we release our webcam, we also release the output
  video.out.release() 

  cv2.destroyAllWindows()
  
  print('done')

def txt_saving():
    user_input = input('Your number?')        
    if int(user_input) == 1:
        save_path = '/home/mendel/AsiaM'
        file_name = 'test_here.txt'
        
        completeName = os.path.join(save_path, file_name)
        print(completeName)
        
        f1 = open(completeName, "w+")
        f1.write("file information")
        f1.close()

class RecordFiles:
  def __init__(self, save_path, file_name, video_format, videoCapture):
    self.save_path = save_path
    self.file_name = file_name
    self.completeName = os.path.join(self.save_path, self.file_name)

    self.format = video_format
    self.fourcc = cv2.VideoWriter_fourcc(*self.format)
    self.cap = cv2.VideoCapture(videoCapture)
    self.out = cv2.VideoWriter(self.completeName, self.fourcc, 20.0, (640, 480))

  def updatePath(self, file_name):
    self.file_name = file_name
    self.completeName = os.path.join(self.save_path, self.file_name)
    
    # Define the codec and create VideoWriter object
    self.out = cv2.VideoWriter(self.completeName, self.fourcc, 20.0, (640, 480))


if __name__ == '__main__':
    print('Script started.')
    parser = argparse.ArgumentParser()
    parser.add_argument('--camera_idx', type=int, help='Index of which video source to use. ', default = 0)
    args = parser.parse_args()
      
    t_format = '%Y%m%d_%H%M%S'
    t_now = datetime.now().replace(microsecond=0)
  
    save_path = '/home/mendel/AsiaM'
    file_name = 'output.mp4'
  
    videoFormat = 'mp4v'
    
    video = RecordFiles(save_path, file_name, videoFormat, args.camera_idx)
    
    try:
        videoCapture(t_now, video)
    except KeyboardInterrupt:
        print('Interrupted')
        video.cap.release()
        video.out.release()
        cv2.destroyAllWindows()
        
print('Terminate')
sys.exit()