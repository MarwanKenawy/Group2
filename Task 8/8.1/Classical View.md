# Classical View

# Imports

- `cv2` imports the OpenCV library for computer vision functionality like image reading/writing, contour detection etc.
- `numpy` imports NumPy for numeric processing like defining color ranges as arrays
- `os` imports the operating system module for file/folder operations

```
import cv2
import numpy as np
import os
```

# Folder Setup

- Define paths to the input image folder and output folder
- Use `os.makedirs()` to create the output folder if it doesn't exist already

```
dataset_folder = './Task8.1_Balls_dataset'
output_folder = './The_output_circles'
```

```
os.makedirs(output_folder, exist_ok=True)
```

# Color Range Definitions

- Defines the minimum and maximum values for HSV/Hue-Saturation-Value color spaces for red and blue
- Each color range is defined as a NumPy array for easier processing
- Two ranges defined per color to account for variations in shades

```
lower_red1 = np.array([0, 100, 150], dtype=np.uint8)
upper_red1 = np.array([10, 255, 255], dtype=np.uint8)
lower_red2 = np.array([160, 100, 100], dtype=np.uint8)
upper_red2 = np.array([180, 255, 255], dtype=np.uint8)
```

```
lower_blue1 = np.array([110, 50, 50], dtype=np.uint8)
upper_blue1 = np.array([130, 255, 255], dtype=np.uint8)
lower_blue2 = np.array([104, 216, 147], dtype=np.uint8)
upper_blue2 = np.array([110, 255, 255], dtype=np.uint8
```

# Process Each Image

- Use `os.listdir()` to get all image filenames in the input folder
- Loop through each image
    - Read the image file
    - Apply Gaussian blur to reduce noise
    - Convert to HSV color space
    - Create masks for red and blue colors using the predefined ranges
    - Find contours in the masks
    - Draw circles and text for qualifying red/blue contours
    - Save the output image

```
images = os.listdir(dataset_folder)

for image_name in images:

  # Read and preprocess image

  # Create masks

  # Find contours

  # Draw circles on red/blue contours

  # Save output
```

# Circle Detection Details

- Filter contours by minimum area to only consider large enough blobs
- Use `cv2.minEnclosingCircle()` to find the smallest circle enclosing each contour
- Calculate contour circularity for filtering non-circular shapes
- Apply circularity thresholding before drawing output circles

```
  if cv2.contourArea(contour) > 200:

     (x, y), radius = cv2.minEnclosingCircle(contour)

     circularity = cv2.contourArea(contour) / (np.pi * radius * radius)

     circularity_threshold = 0.55

     if circularity >= circularity_threshold:

       # Draw circle and text
```

Same for blue contours