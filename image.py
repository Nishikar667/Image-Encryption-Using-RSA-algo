from PIL import Image #importing required libs
import numpy as np 

#encryption
img1 = (Image.open('image.jpeg').convert('L')) 
img1.show()   #showing the image that will be encrypted

img = array((Image.open('image.jpeg').convert('L'))) # converting the RGB image to greyscale  using the .convert() and 'L' aurgument
img32 = np.array(img, dtype=np.uint32) #converting the uint8 type numpy.ndarray to uint32 type
#img = Image.fromarray(img)
#img.save('img.bmp')
a,b = img.shape #counting the no of rows and cols
print('\n\nOriginal image: ')
print(img32)
print((a,b))
tup = a,b # store the number of rows and cols into a tuple

for i in range (0, tup[0]): #going through row 0 to the last row of the matrix 
	for j in range (0, tup[1]): #going through col 0 to the last col of the matrix
		x = img32[i][j] #storing the value of the element into a temp variable
		x = (pow(x,3)%25777) #applying rsa keys 
		img32[i][j] = x #storing back the values to the original matrix
print('\n\nEncrypted image: ')
print(img32)
imgOut = Image.fromarray(img32) #making an image from the matrix
imgOut.show()
##imgOut.save('img.bmp')

#decryption

##img2 = (Image.open('img.bmp').convert('L'))
##img2.show()
img3_32 = img32
img3_32 = np.array(img, dtype=np.uint32)
print('\n\nEncrypted image: ')
print(img3_32)
a1,b1 = img3_32.shape
print((a1,b1))
tup1 = a1,b1

for i1 in range (0, tup1[0]):
	 for j1 in range (0, tup1[1]):
		 x1 = img3_32[i1][j1] 
		 x1 = (pow(x,16971)%25777)	
		 img3_32[i][j] = x1
		 #img3[i1][j1]= (img3[i1][j1] % 256)
print('\n\nDecrypted image: ')
print(img3_32)
imgOut1 = Image.fromarray(img3_32)
imgOut1.show()
#imgOut1.save('img1.bmp')

