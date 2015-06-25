__author__ = 'foury'
import csv
import cv2
import numpy as np

def readCSV(filename):
    if not isinstance(filename, str):
        raise TypeError('please enter right path of the csv file')
    with open(filename,'rb') as f:
        f_csv=csv.reader(f)
        M=[]
        for row in f_csv:
            m = cv2.imread(row[0])
            m=m[:,:,0]
            M.append(m)




    return M



