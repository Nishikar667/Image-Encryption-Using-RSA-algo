#TODO exception handling 

import cv2 as cv 
import numpy as np
import png
import imageio 
import time
from tqdm import tqdm 
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

start = time.time()

image_window = Tk()
image_window.geometry ( '350x200' )
image_window.title ('Image Cryptography')

def goback():
	exit()

def powmod(b, e, m):
	b2 = b
	res = 1
	while e:
		if e & 1:
			res = (res * b2) % m   
		b2 = (b2*b2) % m        
		e >>= 1                 
	return res

def filenameerror():
	messagebox.showinfo('Error Occured!', 'Please select a 8bit/16bit Image File')

def enfinish():
	messagebox.showinfo('Done!', 'Encryption is finished and saved as EnImage.png')

def definish():
	messagebox.showinfo('Done!', 'Decryption is finished and saved as DeImage.png')

def encrypt():

	try:
			
		if(messagebox.askyesno('Select Mode', 'Do you want to have it as greyscale? ') == True): 
		
			img = cv.imread(askopenfilename(), 0)
			#print(type(img))
			img = img.astype(np.uint16)
			a,b = img.shape
			print('\n\nOriginal image: ')
			print(img)
			print((a,b))
			tup = a,b
			for i in tqdm(range(0, tup[0])):
				for j in (range(0, tup[1])):
					x = img[i][j] 
					x = (pow(x,3)%25777)
					img[i][j] = x
			print('\n\nEncrypted Image:\n\n')
			print(img)
			#cv.imshow('EnImage', img)
			cv.imwrite('EnImg.png', img)
			end = time.time()
			eTime = end - start
			print(eTime)

			enfinish()
			
			myframe = ttk.Frame(image_window)
			myentry = ttk.Entry(myframe, textvariable=img, state='readonly')               ##TODO this is not working 
			myscroll = ttk.Scrollbar(myframe, orient='vertical', command=myentry.xview)
			myentry.config(xscrollcommand=myscroll.set)
				
			myframe.place()
			myentry.place(x=30, y=30)
			myscroll.place(x=40, y=40)
			image_window.mainloop()

		else:
			
			img = cv.imread(askopenfilename())
			#print(type(img))
			img = img.astype(np.uint16)
			a = img.shape
			print('\n\nOriginal image: ')
			print(img)
			print(a)

			img= img.tolist()
			for i in tqdm(range(len(img))):
				for j in (range(len(img[i]))):
					for k in (range(len(img[i][j]))):
						x = img[i][j][k] 
						x = (pow(x,3)%25777)
						img[i][j][k] = x

			img = np.array(img).astype(np.uint16)
			imageio.imwrite('EnImage.png', img, format='PNG-FI')

			print('\n\nEncrypted Image:\n\n')
			print(img)

			enfinish()

			myframe = ttk.Frame(image_window)
			myentry = ttk.Entry(myframe, textvariable=img, state='readonly')
			myscroll = ttk.Scrollbar(myframe, orient='vertical', command=myentry.xview)
			myentry.config(xscrollcommand=myscroll.set)
				
			myframe.place()
			myentry.place(x=30, y=30)
			myscroll.place(x=40, y=40)
			image_window.mainloop()
		
	except TypeError:
		filenameerror()

	except AttributeError:
		filenameerror()
				
			

def decrypt():

	try:
	
		if(messagebox.askyesno('Select Mode', 'Do you want to have it as greyscale? ') == True): 
				
			img1 = imageio.imread(askopenfilename())
			print('\n\nReading Encrypted Image again:\n\n')
			print(img1)

			#for g in tqdm(range(100)):
			img1= img1.tolist()
			print('Decrypting....')
			for i1 in tqdm(range(len(img1))):
				for j1 in (range(len(img1[i1]))):
					x1 = img1[i1][j1] 
					x1 = powmod(x1,16971,25777)
					img1[i1][j1] = x1

			img1 = np.array(img1)#.reshape(184,275)
			print('\n\nDecrypted Image:\n\n')
			print(img1)
			#cv.imshow('DeImage', img1)
			cv.imwrite('DeImage.png', img1)

			end = time.time()
			eTime = end - start
			print(eTime)
			
			definish()

		else:

			img1 = imageio.imread(askopenfilename(), format='PNG-FI')
			print('\n\nReading Encrypted Image again:\n\n')
			print(img1)
			img1= img1.tolist()
			print('Decrypting....')

			for i1 in tqdm(range(len(img1))):
				for j1 in (range(len(img1[i1]))):
					for k1 in (range(len(img1[i1][j1]))):
						x1 = img1[i1][j1][k1] 
						x1 = powmod(x1,16971,25777)
						img1[i1][j1][k1] = x1

			img1 = np.array(img1)#.reshape(184,275)
			print('\n\nDecrypted Image:\n\n')
			print(img1)
			cv.imwrite('DeImage.png', img1)

			end = time.time()
			eTime = end - start
			print(eTime)
		
			definish()
	
	except TypeError:
		filenameerror()

	except AttributeError:
		filenameerror()

btn_decrypt = Button( image_window, text = "Image Decryption", command = decrypt)
btn_decrypt.place( x=20, y=100 )
#btn_decrypt.bind('<Return>', decrypt)
btn_encrypt = Button( image_window, text = "Image Encryption", command = encrypt)
btn_encrypt.place( x=200, y=100 )
#btn_encrypt.bind('<Return>', encrypt)
btn_exit = Button( image_window, text = "Go Back" , command = goback).place( x=140, y=150 )
image_window.mainloop()

