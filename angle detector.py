import cv2 as cv
import numpy as np
import math 

pro=cv.imread(r'C:\Users\Atul Kumar\Documents\roboism\after end sem\opencv\f4352e0f07a60bb07b038bd895c3163b.jpg')
#img = np.zeros([512, 512, 3], np.uint8)
w,h = 512,512
img = cv.resize(pro, (w,h))
pointlist=[]
def click_mouse_event(event,x,y,flags,params):
    if event==cv.EVENT_LBUTTONDOWN:
        pointlist.append([x,y])
        font =cv.FONT_HERSHEY_DUPLEX
        clc=cv.circle(img,(x,y),3,(0,255,255),-1)
        print(pointlist)
        cv.imshow("image",clc)

def gradient(a,b):
    return (b[1]-a[1])/(b[0]-a[0])

def angle(x):
    pt1,pt2,pt3=pointlist[-3:]
    m1=gradient(pt1,pt2)
    m2=gradient(pt1,pt3)
    angR=(math.atan(math.fabs((m1-m2)/(1+m2*m1))))
    angD=round(math.degrees(angR))
    if angD<0:
        angD=angD+180
    font =cv.FONT_HERSHEY_DUPLEX
    clc=cv.putText(img,str(angD),(pt1[0],pt1[1]),font,1,(0,0,255),1)
    



while True:
    cv.imshow("image",img)
    cv.setMouseCallback("image",click_mouse_event)
    if len(pointlist)%3==0 and len(pointlist)!=0:
       pt1,pt2,pt3=pointlist[-3:]
       clc = cv.arrowedLine(img, (pt1[0],pt1[1]), (pt2[0],pt2[1]), (0, 255, 255), 5)
       clc = cv.arrowedLine(img, (pt1[0],pt1[1]), (pt3[0],pt3[1]), (0, 255, 255), 5)
       angle(pointlist)
    if cv.waitKey(1) & 0xFF==ord('e'):
        pointlist=[]
        img = cv.resize(pro, (w,h))
    cv.destroyAllWindows    

