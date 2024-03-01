import cv2
import numpy as np
from itertools import chain


Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Uvalde_2.jpg'

Image = cv2.imread(Image_Path)

def Stack_Images(Scale=(100,100),List_Images=[]):
	
	H_Stack = []
	V_Stack = []
	a,i,b= 0,0,0
	Rows = len(List_Images)
	Columns = len(max(List_Images,key=len))

	for row in range(Rows):
		for column in range(Columns):
			try:
				List_Images[row][column]
			except IndexError as e:
				Blank_Image = np.zeros((*Scale,3),np.uint8)
				List_Images[row].append(Blank_Image)
				print('EXception')

			# Resizing the image
			List_Images[row][column] = cv2.resize(List_Images[row][column],Scale)
			if (column*Columns)>= (Rows*Columns)//2:
				H_Stack.append(List_Images[row][column])
				i+=1
			else:
				V_Stack.append(List_Images[row][column])
				a+=1
			b+=1
	print("Row: ",Rows)
	print("Columns: ",Columns)
	print("H_Stack: ",len(H_Stack))
	print("V_Stack: ",len(V_Stack))
	print('a: ',a)
	print("i: ",i)
	print('b: ',b)
	print(V_Stack[0].shape)
	E,F,_ = V_Stack[0].shape
	e,f = Scale

	# n = np.zeros((E*i,F*b,3),np.uint8)
	# print(n.shape)
	# print('n')
	# h,w = n.shape[0],n.shape[1]

	# n[w//2:][0:] = np.hstack(H_Stack)
	# n[:w//2][0:] = np.hstack(V_Stack)
	cv2.imshow("F",np.hstack((list(chain(*List_Images)))))
	# x = np.array(list(chain(*List_Images)))
	# cv2.imshow('H',np.hstack(H_Stack))
	# cv2.imshow('V',np.hstack(V_Stack))
	# cv2.imshow("Frame2",np.hstack(list(chain(*List_Images))))
	cv2.waitKey(0)

# Stack_Images((200,300),[[Image,Image,Image],[Image,Image],[Image,Image,Image,Image]])
Stack_Images((200,300),[[Image,Image,Image]])