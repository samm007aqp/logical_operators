import cv2
import numpy as np 
from matplotlib import pyplot as plt 

def Th(img,row,col,x):
	for i in range(row):
		for j in range(col):
			val = img[i,j] 
			if val > x:
				img[i,j] = 255
			else:
				img[i,j] = 0
def Not(img,row,col):
	for i in range(row):
		for j in range(col):
			img[i,j] = 255- img[i,j]

img = cv2.imread("log_3.png")
img2 = cv2.imread("log_4.png")

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

row,col = img.shape
r, c = img2.shape

Not(img,row,col)
Not(img2,r,c)
Th(img,row,col,100)
Th(img2,r,c,100)
cv2.imshow('img1',img)
cv2.imshow('img2',img2)

for i in range (row):
	for j in range(col):
		img[i,j] = img[i,j] & img2[i,j]





cv2.imshow('salida',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#binario = '{0:08b}'.format(img[0,0])
#bina = bin(img[0,0])
#print(type(binario) )
#print(type(bina) )

