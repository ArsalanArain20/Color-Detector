# Imports
import cv2
from utility import Color_Range
from PIL import Image
import os

blue = [255, 0, 0]  # Red in BGR color space
cap = cv2.VideoCapture(1)

# Path to store the video file (Only use when we want to Store Video)
"""
output_folder =  r'folder path here '
output_video_path = os.path.join(output_folder, 'output_video.avi')

# Define the codec and create VideoWriter object (XVID for .avi files)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (900, 600))
"""

while cap.isOpened():
    success, frame = cap.read()
    if success:
        frame = cv2.resize(frame, (900, 600))
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert BGR to HSV

        # Get the HSV range for red color
        lower_limit, upper_limit = Color_Range(color=blue)

        # Create a mask with the red color range
        mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

        mask_ = Image.fromarray(mask)
        box = mask_.getbbox()
        if box is not None:
            x1, y1, x2, y2 = box
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 6)  # 6 is the thickness

        # Write the frame to the video file (use when we want to store it)
        # out.write(frame)

        # Display the frame with the bounding box
        cv2.imshow('Live', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
