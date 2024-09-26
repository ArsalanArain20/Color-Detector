import numpy as np
import cv2

def Color_Range(color):
    """
    This Function get a input of any colour and then its give colour range of the inputed color range value of HUE
    :param color:
    :return:
    """
    # Convert BGR color list to a 1x1 pixel image (shape: 1x1x3)
    c = np.uint8([[color]])  # Reshaping to 1x1x3
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # Get the HUE value from the converted HSV color, cast it to an integer to avoid overflow
    hue_value = int(hsvC[0][0][0])

    # Safely calculate lower and upper limits for HUE
    lower_hue = max(hue_value - 10, 0)  # Ensuring the value doesn't go below 0
    upper_hue = min(hue_value + 10, 179)  # Ensuring the value doesn't exceed 179

    # Define the lower and upper limits for HSV
    lower_limit = np.array([lower_hue, 100, 100], dtype=np.uint8)
    upper_limit = np.array([upper_hue, 255, 255], dtype=np.uint8)

    return lower_limit,upper_limit