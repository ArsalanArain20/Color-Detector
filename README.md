# Color Detector

**Color Detector** is a live color detection project built using the OpenCV (cv2) library. This tool detects specific colors in a live video stream, identifies shapes with the target color, and creates a bounding box around them. The project uses color space conversion to HSC, detects target shapes using a mask, and outlines them in real-time.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project works as a real-time color detector using OpenCV. The application:
1. Converts the live frame into **HSC (Hue, Saturation, Chroma)** color space.
2. Uses a mask to detect shapes with the target color.
3. Draws a bounding box around the detected shape based on the selected color.

The color boundaries used to generate the mask are provided by a utility file, `utility.py`. This file helps by defining the boundary values for specific colors to facilitate shape detection in the main file, `home.py`.

## Installation

### Prerequisites
- **Python 3.x**
- **OpenCV (cv2)**

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ColorDetector.git
   cd ColorDetector