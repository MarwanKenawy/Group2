import cv2
import numpy as np
#-----------------------------------
#this is a way to select the 2 images you want 
#import tkinter as tk
#from tkinter import filedialog
#Create a Tkinter window
#path= tk.Tk()
#path.withdraw()
# select the left,right image file
#imgL_path=filedialog.askopenfilename(title="imgL")
#imgR_path=filedialog.askopenfilename(title="imgR")
# Load left,right images
#imgL=cv2.imread(imgL_path)
#imgR=cv2.imread(imgR_path)
#----------------------------------
#another way to upload images
# Load left,right images
imgL=cv2.imread('Downloads/left_image.jpg')
imgR= cv2.imread('Downloads/right_image.jpg')
# Denoise left,right images with adjusted parameters
#fastNlMeansDenoisingColored is fn to remove noise ,its parameters(input image,destination image,h,hForColorComponents,templateWindowSize,searchWindowSize),default values.
imgL_d= cv2.fastNlMeansDenoisingColored(imgL,None,10,10,7,21)
imgR_d= cv2.fastNlMeansDenoisingColored(imgR,None,10,10,7,21)
# Resize denoised images
scale_factor= 3
imgL_resized= cv2.resize(imgL_d,None,fx=scale_factor,fy=scale_factor)
imgR_resized= cv2.resize(imgR_d,None,fx=scale_factor,fy=scale_factor)
# Convert to grayscale
imgL_GRY= cv2.cvtColor(imgL_resized,cv2.COLOR_BGR2GRAY)
imgR_GRY= cv2.cvtColor(imgR_resized,cv2.COLOR_BGR2GRAY)
# Compute disparity map using StereoBM
stereo= cv2.StereoBM_create(numDisparities=32,blockSize=5)
disparity= stereo.compute(imgL_GRY,imgR_GRY)
# Convert disparity to depth using camera parameters
focal_length=0.7
baseline= 0.06  # distance between the cameras in meters
depth= (focal_length * baseline)/(disparity+0.0001)#0.0001 to avoid dividing by zero
# Normalize and display depth map
min_depth= depth.min()
max_depth= depth.max()
depth_norm= np.uint8((depth-min_depth)/(max_depth-min_depth)*255)

cv2.imshow('Depth Map',depth_norm)
cv2.imshow('Left',imgL)
cv2.imshow('Right',imgR)
cv2.waitKey(0)
cv2.destroyAllWindows()
