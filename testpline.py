import numpy as np
import cv2
import math as m

port = 0

frame =30
#Taking video capture
camera = cv2.VideoCapture(port)

while (camera.isOpened()):
    ret,img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #taking out the edges
    edge = cv2.Canny(gray,100,200,apertureSize=3)
    #taking out lines
    line = cv2.HoughLinesP(edge,1,np.pi/180,100,0,10)
    if line is not None:

            for (x1,y1,x2,y2) in line[0]:
                if x2==x1:
                    cv2.line(gray,(x1,y1), (x2,y2), (0,0,0),10)
                    
                    if line.any()==True:
                        d = m.sqrt(m.pow((x2-x1),2)+m.pow((y2-y1),2))
                        print d
                        print "Line Detected" 
                else:
                    print "Line not Detected"          
            cv2.imshow("line",gray)
                
            k = cv2.waitKey(1)
            if k==27:
               break
    else:
        print "Line not detected"
    #'http://192.168.43.1:8080/'
