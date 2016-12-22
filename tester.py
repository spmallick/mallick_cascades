#!/usr/local/bin/python

import numpy as np
import cv2
import sys
import os

if __name__ == '__main__' :

    if len(sys.argv) < 2 :
        print 'Usage : \n python tester.py haarcascades/haarcascade_frontalface.xml'
        exit(0)

    cascade_name = sys.argv[1]
    dirname, filename = os.path.split(cascade_name)
    mallick_filename = 'mallick_' + filename
    mallick_cascade_name = os.path.join(dirname, mallick_filename)
    object_cascade = cv2.CascadeClassifier(cascade_name)
#    mallick_object_cascade = cv2.CascadeClassifier(mallick_cascade_name)
    cap = cv2.VideoCapture(0);
    font = cv2.FONT_HERSHEY_SIMPLEX
    red = (0,0,255)
    blue = (255,0,0)
    while True :
        ret, img = cap.read()
        img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        objects = object_cascade.detectMultiScale(gray, 1.3, 5)
        #       mallick_objects = mallick_object_cascade.detectMultiScale(gray, 1.3, 5)
        mallick_objects = []
        for (x,y,w,h) in objects:
            img = cv2.rectangle(img,(x+2,y+2),(x+w-4,y+h-4), blue,2)
        for (x,y,w,h) in mallick_objects:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),red,2)

        if len(objects) > 0 :
            cv2.putText(img, filename,(10,30), font, 0.5, blue,2,cv2.LINE_AA)
        if len(mallick_objects) > 0 :
            cv2.putText(img, mallick_filename,(10,50), font, 0.5,red,2,cv2.LINE_AA)


        cv2.imshow('img',img)
        key = 0xFF & cv2.waitKey(1)
        if key == 27:
            break

    cv2.destroyAllWindows()