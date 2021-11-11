# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 17:25:15 2021

@author: Admin
"""

import numpy as np
import os 

import argparse
import cv2

from datetime import datetime

import sys


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--camera_idx', type=int, help='Index of which video source to use. ', default = 0)
        args = parser.parse_args()
        
        args.camera_idx
        cap = cv2.VideoCapture(args.camera_idx)
        
        t_format = '%Y%m%d_%H%M%S'
        t_now = datetime.now()
        
        save_path = '/home/mendel/AsiaM'
        file_name = 'output_' + t_now.strftime(t_format) + '.mp4'
        completeName = os.path.join(save_path, file_name)
        
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = 30
        dim = (640, 480)
        out = cv2.VideoWriter(completeName, fourcc, fps, dim)
        
        print('start')
        x = 0
        while cap.isOpened():
            ret, frame = cap.read()
        
            if not ret:
              print('welp')
              break
        
            cv2_im = frame
            x += 1
            # output the frame
            out.write(cv2_im) 
            
            if (datetime.now() - t_now).seconds > 10:
                out.release()
                #print('saved')
                #print(x)
                x = 0
                t_now = datetime.now()
                file_name = 'output_' + t_now.strftime(t_format) + '.mp4'
                completeName = os.path.join(save_path, file_name)
                
                # Define the codec and create VideoWriter object
                out = cv2.VideoWriter(completeName, fourcc, fps, dim)
                
        cap.release()
    
        # After we release our webcam, we also release the output
        out.release() 
    
        cv2.destroyAllWindows()
      
        print('done')
        
    except KeyboardInterrupt:
        print('Interrupted')
        cap.release()
        out.release()
        cv2.destroyAllWindows()
print('Terminate')
sys.exit()