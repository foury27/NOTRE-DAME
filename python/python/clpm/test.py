__author__ = 'foury'
import numpy as np
import cv2
a=cv2.imread("")
down=cv2.pyrDown(a)
down=cv2.pyrDown(down)
down2=cv2.pyrDown(down)
cv2.imwrite("/Users/foury/Documents/github/amygit/FR/FR_SR/FR_SR/testimg2/high/high_downsampled/high/20.jpg",down)
cv2.imwrite("/Users/foury/Documents/github/amygit/FR/FR_SR/FR_SR/testimg2/high/low_downsampled/low/20.jpg",down2)