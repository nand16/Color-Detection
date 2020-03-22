import cv2
import pandas as pd
import numpy as np
#import math


click=False
r=g=b=xpos=ypos=0
img=cv2.imread("three.jpg")
index=["color","color_name","hexa","r","g","b"]
data=pd.read_csv("colors.csv",names=index,header=None)


def getName(r,g,b):
    m=100000
    for i in range(len(data)):
        dis=np.sqrt(((r-int(data.loc[i,"r"]))**2)+((g-int(data.loc[i,"g"]))**2)+((b-int(data.loc[i,"b"]))**2))
        if(dis<m):
            m=dis
            color=data.loc[i,"color_name"]
    return(color)
    
def draw_function(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global r,g,b,click,xpos,ypos
        click=True
        xpos=x
        ypos=y
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)
    
cv2.namedWindow("Color dectection Window")
cv2.setMouseCallback("Color dectection Window",draw_function)

while(True):
    cv2.imshow("Color dectection Window",img)
    if(click):
        cv2.rectangle(img,(50,15),(900,60),(b,g,r),-1)
        text=getName(r,g,b)+" R = "+str(r)+" G = "+str(g)+" B = "+str(b)
        cv2.putText(img,text,(140,45),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if(r+g+b>=600):
            cv2.putText(img,text,(140,45),2,0.8,(0,0,0),2,cv2.LINE_AA)
        click=False
    if cv2.waitKey(10) & 0xFF==27:
        break
    
cv2.destroyAllWindows()