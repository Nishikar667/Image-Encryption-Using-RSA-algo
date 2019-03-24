import cv2 as cv 
import numpy as np
import imageio 

img = cv.imread('image.jpeg', 0)
#print(type(img))
img = img.astype(np.uint16)
a,b = img.shape
print('\n\nOriginal image: ')
print(img)
print((a,b))
tup = a,b

for i in range (0, tup[0]):
	for j in range (0, tup[1]):
		x = img[i][j] 
		x = (pow(x,3)%25777)
		img[i][j] = x

print(img)
cv.imshow('EnImage', img)
cv.imwrite('newgrey.png', img)



img1 = imageio.imread('newgrey.png')
print(img1)
img1= img1.tolist()

for i1 in range(len(img1)):
	for j1 in range(len(img1[i])):
		
		x1 = img1[i1][j1] 
		x1 = (pow(x1,16971)%25777)
		img1[i1][j1] = x1

img1 = np.array(img1)#.reshape(184,275)
print(img1)
cv.imshow('DeImage', img1)
cv.imwrite('newgrey.png', img1)
