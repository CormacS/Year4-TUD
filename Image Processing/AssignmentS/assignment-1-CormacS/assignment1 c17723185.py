import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui
import tkinter as tk

#More indetail explination in the word file.


#Function for faded image
def fadedImage():
    f = easygui.fileopenbox()
    original = cv2.imread(f)
    I = original.copy()
    gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)

    #Used GaussianBlur to remove noise
    blur = cv2.GaussianBlur(gray,(7,7),1)

    #Used Canny to detect the edges of the faded section
    edges = cv2.Canny(blur,85,80)

    #Houghlines got me the coordinates of the lines
    lines = cv2.HoughLinesP(edges,1,np.pi/180,95 ,60,30)

    #Found min and max values for x1,x2,y1,y2
    counter = 0
    for line in lines:
        for x1,y1,x2,y2 in line:
            if counter == 0:
                minX = x1
                minY = y1
                maxX = x2
                maxY = y2
            else:
                if x1 < minX:
                    minX = x1 
                
                if y1 < minY:
                    minY = y1

                if x2 > maxX:
                    maxX = x2

                if y2 > maxY:
                    maxX = y2   
        counter+=1

    #Cut out faded part of image
    faded = I[minY:maxY,minX:maxX]

    #Reduced the faded part
    corrected = faded - 32

    #Put corrected section back into image
    I[minY:maxY,minX:maxX] = corrected

    #Made a mask
    mask = I.copy()
    mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
    mask[:,:] = (0)

    #Drew a white box on the mask
    cv2.line(mask,(minX,minY),(maxX,minY),(255,255,255),2)
    cv2.line(mask,(maxX,minY),(maxX,maxY),(255,255,255),2)
    cv2.line(mask,(maxX,maxY),(minX,maxY),(255,255,255),2)
    cv2.line(mask,(minX,maxY),(minX,minY),(255,255,255),2)

    #Used inpaint to fill in the white box
    dst = cv2.inpaint(I,mask,3,cv2.INPAINT_TELEA)

    cv2.imshow("Original", original)
    cv2.imshow("Restored", dst)
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()

def damagedImage():
    f = easygui.fileopenbox()
    original = cv2.imread(f)
    I = original.copy()

    #Converted to HSV to reduce saturation
    hsv =cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    s = s*0.05
    
    #Converted it to uint8
    s = s.astype('uint8')
    hsv = cv2.merge( (h,s,v))
    I = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

    grey = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)

    #Used inRange to create masks from white spots
    mask = cv2.inRange(grey,190,255)

    #Used inpaint to remove white spots
    I = cv2.inpaint(I,mask,10,cv2.INPAINT_TELEA)

    cv2.imshow('Original',original)
    cv2.imshow('Restored',I)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#GUI that asks the user to select what type of image they want to restore?
root = tk.Tk()
root.title('Assignment 1: Restoring Images')
button1 = tk.Button(root,text="Quit", fg="red",command=quit)
button2 = tk.Button(root,text="Faded Image",height=10,width=25, command=fadedImage)
button3 = tk.Button(root,text="Damaged Image",height=10,width=25,command=damagedImage)

button2.grid(column=0, row=1)
button3.grid(column=2, row=1)
button1.grid(column=1, row=2)

root.mainloop()