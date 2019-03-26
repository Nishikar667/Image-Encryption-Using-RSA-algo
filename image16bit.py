import cv2 as cv 
import numpy as np
import imageio 

img = cv.imread('image.jpeg', 0) # 0 to read the image as greyscale
#print(type(img))
img = img.astype(np.uint16) '''as the input image is .jpeg which is a 8bit depth image 
                               we need to convert the numpy.ndarray of the image to 16bit 
			       numpy.ndarray which can store data upto 2^16-1 in decimal'''
a,b = img.shape #reading the rows and cols of the image
print('\n\nOriginal image: ')
print(img) #print the array
print((a,b))
tup = a,b

for i in range (0, tup[0]): #tup[0] will is the no. of rows
	for j in range (0, tup[1]): #tup[0] is the no. of cols
		x = img[i][j] #store the particular pixel value to a int64 type variable temporarily
		x = (pow(x,3)%25777) #apply the rsa key (3, 25777)
		img[i][j] = x #store the value back to the array

print(img) #print the encrypted array
cv.imshow('EnImage', img)
cv.imwrite('newgrey.png', img) #save the array as 16bit depth .png image

#decryption

img1 = imageio.imread('newgrey.png')#read the image as 16bit per channel image
print(img1)
img1= img1.tolist() #converting the 2d array to a list of lists

for i1 in range(len(img1)): # loop through the list and apply the key
	for j1 in range(len(img1[i])):
		
		x1 = img1[i1][j1] 
		x1 = (pow(x1,16971)%25777)
		img1[i1][j1] = x1

img1 = np.array(img1)#.reshape(184,275)
print(img1)
cv.imshow('DeImage', img1)
cv.imwrite('newgrey.png', img1)  #save the decrypted image as 16bit depth image
