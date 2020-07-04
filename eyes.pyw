import numpy as np
import cv2
import time

eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
smh = cv2.imread('sharingan.png')
bitch = cv2.imread('byakugan.png')
rin = cv2.imread('rinnegan.png')

m1 = 1;
m2 = 1;
eye = 0;
mx,my = 0,0;

def idontknowwhatiamdoing(event,x,y,flags,param):
    global m1
    if event == cv2.EVENT_LBUTTONDOWN:
        if(x >= 100 and x <= 540 and y >= 170 and y <= 240):
            m1 = 0
        if(x >= 100 and x <= 540 and y >= 250 and y <= 320):
            cv2.destroyAllWindows()
            exit(0)

def godineedhelp(event,x,y,flags,param):
    global m2
    global eye
    if event == cv2.EVENT_LBUTTONDOWN:
        if(x >= 100 and x <= 540 and y >= 150 and y <= 220):
            eye,m2 = 1, 0
        if(x >= 100 and x <= 540 and y >= 240 and y <= 310):
            eye,m2 = 2, 0
        if(x >= 100 and x <= 540 and y >= 330 and y <= 400):
            eye,m2 = 3, 0

def snakey(event,x,y,flags,param):
    global mx
    global my
    if event == cv2.EVENT_LBUTTONDOWN:
        mx,my = x,y
    else:
        mx,my = 0,0

while m1:
    img = np.zeros((480,640,3), np.uint8)
    cv2.setMouseCallback('Narutoooo!', idontknowwhatiamdoing)
    cv2.rectangle(img,(0,0),(640,480),(216,191,216),-1)
    cv2.rectangle(img,(100,170),(540,240),(0,255,255),-1)
    cv2.rectangle(img,(100,250),(540,320),(0,255,255),-1)
    cv2.putText(img,'EYE THING', (240,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    cv2.putText(img,'START', (280,215), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    cv2.putText(img,'STOP', (285,295), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    cv2.imshow('Narutoooo!',img)
    cv2.waitKey(30)
    if cv2.getWindowProperty('Narutoooo!',cv2.WND_PROP_AUTOSIZE) == -1:        
        cv2.destroyAllWindows()
        exit(0)

cv2.destroyAllWindows()

while m2:
    img = np.zeros((480,640,3), np.uint8)
    cv2.setMouseCallback('yes', godineedhelp)
    cv2.rectangle(img,(0,0),(640,480),(216,191,216),-1)
    cv2.rectangle(img,(100,150),(540,220),(0,255,255),-1)
    cv2.rectangle(img,(100,240),(540,310),(0,255,255),-1)
    cv2.rectangle(img,(100,330),(540,400),(0,255,255),-1)

    cv2.putText(img,'CHOOSE YOUR DOJUSTU!', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    cv2.putText(img,'Byakugan', (250,185), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    cv2.putText(img,'Sharingan', (250,275), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    cv2.putText(img,'Rinnegan', (255,365), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    
    cv2.imshow('yes',img)
    cv2.waitKey(30)
    if cv2.getWindowProperty('yes',cv2.WND_PROP_AUTOSIZE) == -1:        
        cv2.destroyAllWindows()
        exit(0)

cv2.destroyAllWindows()
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)
    nr_ochi = 0
    permh = 0
    permw = 0
    for (ex,ey,ew,eh) in eyes:
        #cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),5)
        nr_ochi = nr_ochi+1
        if(nr_ochi == 1):
            permh = eh
            premw = ew
        if(eye == 1):
            draw = cv2.resize(bitch, (permh, premw), interpolation = cv2.INTER_AREA)
        elif(eye == 2):
            draw = cv2.resize(smh, (permh, premw), interpolation = cv2.INTER_AREA)
        elif(eye == 3):
            draw = cv2.resize(rin, (permh, premw), interpolation = cv2.INTER_AREA)
        for i in range(0, permh-1):
            for j in range(0, premw-1):
                img[ey+i][ex+j] = draw[i][j]
        if(nr_ochi == 2):
            break
    cv2.imshow('hinata thicc tho',img)
    cv2.waitKey(30)
    if cv2.getWindowProperty('hinata thicc tho',cv2.WND_PROP_AUTOSIZE) == -1:        
        break

cap.release()
cv2.destroyAllWindows()
exit(0)
