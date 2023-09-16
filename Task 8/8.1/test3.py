import cv2
import numpy as np
import os

# Load the images
dataset_folder = './Task8.1_Balls_dataset' 
output_folder = './The_output_circles' 

# Check if the folder is found(if not found, create a new one)
os.makedirs(output_folder, exist_ok=True)

lower_red1 = np.array([0, 100, 150], dtype=np.uint8)
upper_red1 = np.array([10, 255, 255], dtype=np.uint8)
lower_red2 = np.array([160, 100, 100], dtype=np.uint8)
upper_red2 = np.array([180, 255, 255], dtype=np.uint8)

lower_blue = np.array([110, 50, 50], dtype=np.uint8)
upper_blue = np.array([130, 255, 255], dtype=np.uint8)

images = os.listdir(dataset_folder)

for image_name in images:
    # Read the image
    image_path = os.path.join(dataset_folder, image_name)
    img = cv2.imread(image_path)


    # Apply a Gaussian blur to the image to reduce noise
    img_blurred = cv2.GaussianBlur(img, (15, 15), 0)
    hsv_img = cv2.cvtColor(img_blurred, cv2.COLOR_BGR2HSV)

    # Create masks for red and blue colors
    mask1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)
    
    blue_mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

    # Find contours in the masks
    red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter and draw circles 
    for contour in red_contours:
        if cv2.contourArea(contour) > 200:  
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            
            # Calculate circularity 
            circularity = cv2.contourArea(contour) / (np.pi * radius * radius)
            
            # Set a circularity threshold to filter out non-circular objects
            circularity_threshold = 0.55 
            
            if circularity >= circularity_threshold:
                cv2.circle(img, center, radius, (0, 0, 255), 2)
                cv2.putText(img, 'Red Ball', (int(x - radius), int(y - radius - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                
    for contour in blue_contours:
        if cv2.contourArea(contour) > 200:  
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            
            # Calculate circularity 
            circularity = cv2.contourArea(contour) / (np.pi * radius * radius)
            
            # Set a circularity threshold to filter out non-circular objects
            circularity_threshold = 0.45
            
            if circularity >= circularity_threshold:
                cv2.circle(img, center, radius, (255, 0, 0), 2)
                cv2.putText(img, 'Blue Ball', (int(x - radius), int(y - radius - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Save the image with circle detections
    output_path = os.path.join(output_folder, image_name)
    cv2.imwrite(output_path, img)