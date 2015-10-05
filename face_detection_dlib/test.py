__author__ = 'foury'
import dlib
import cv2
import os
pics=os.listdir("/Users/foury/Documents/github/amygit/NOTRE-DAME/face_detection_dlib/stills/")
for pic in pics:

    img_ori=cv2.imread("/Users/foury/Documents/github/amygit/NOTRE-DAME/face_detection_dlib/stills/"+pic)
    img = cv2.resize(img_ori,None, fx=0.5,fy=0.5, interpolation = cv2.INTER_AREA)

    detector = dlib.get_frontal_face_detector()
    faces = detector(img)
    for d in faces:
        print "left,top,right,bottom:", d.left(), d.top(), d.right(), d.bottom()
        cv2.rectangle(img,(d.left(),d.top()),(d.right(),d.bottom()),255)
        face=img[d.top():d.bottom(),d.left():d.right()]
        cv2.imwrite("/Users/foury/Documents/github/amygit/NOTRE-DAME/face_detection_dlib/Pasc_faces/"+pic,face)
        #cv2.imshow("this",face)
        #cv2.waitKey(1000)