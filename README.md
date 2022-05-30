# APO_Softwart

One of my first serious project. It's a simple image processing software, which allow to show histogram, reduce grayscale or stretch histogram.

My last commit was at least 2 months ago and I completely changed my entire project.

First of all, I rebuild adding images system. In first version we could make operations in only one image in one window. Now you can add as many images as you can and make operations on all of them.

The next things are operations. In first version you could show histogram and... Well, you could only show histogram. After 2 months I finally made this app useful and added 14(!) new function. Let me enumerate them:
- Negation
- Threshold
- Threshold with grayscale
- Binarization
- Histogram stretching
- Posterization
- Equalization
- Blur linear smoothing
- Gaussian Blur linear smoothing
- Laplacian edge detection
- Sobel edge detection
- Canny edge detection
- Linear defuzzification with 3 Laplacian masks
- Directional edge detection with 8 basic Prewitt masks

# How to run APO_Software
```
$ git clone https://github.com/JakubKosakowski/APO_Software.git

$ cd APO_Software

$ python -m venv venv

$ venv\Scripts\activate.bat

$ pip install -r requirements.txt

$ python main_window.py
```
