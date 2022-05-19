import cv2
import numpy as np
from PIL import Image

class Operations:
    def __init__(self, photo):
        self.photo = photo.copy()

    def negation(self):
        for i in range(len(self.photo)):
            for j in range(len(self.photo[i])):
                for k in range(3):
                    self.photo[i][j][k] = 255 - self.photo[i][j][k]
        return self.photo

    def set_default(self, photo):
        self.photo = photo.copy()

    def user_mask(self, mask, border):
        border_type = self.set_border_type(border)
        mask_type = self.set_mask(mask)
        kernel = np.zeros((3,3))

        for i in range(3):
            for j in range(3):
                kernel[i,j] = mask_type[i,j]

        kernel = np.int64(kernel)/np.sum(kernel)

        self.photo = cv2.filter2D(self.photo, cv2.CV_8UC1, kernel, borderType=border_type)
        return self.photo

    def threshold(self, param1, param2):
        for i in range(len(self.photo)):
            for j in range(len(self.photo[i])):
                for k in range(3):
                    if (self.photo[i][j][k] <= param2 and self.photo[i][j][k] >= param1):
                        self.photo[i][j][k] = 255
                    else:
                        self.photo[i][j][k] = 0
        return self.photo

    def grayscale_threshold(self, param):
        for i in range(len(self.photo)):
            for j in range(len(self.photo[i])):
                for k in range(3):
                    if (self.photo[i][j][k] < param):
                        self.photo[i][j][k] = 0
        return self.photo

    def binarization(self, param):
        for i in range(len(self.photo)):
            for j in range(len(self.photo[i])):
                for k in range(3):
                    if (self.photo[i][j][k] <= param):
                        self.photo[i][j][k] = 255
                    else:
                        self.photo[i][j][k] = 0
        return self.photo

    def histogram_stretching(self):
        im_min = np.min(self.photo)
        im_max = np.max(self.photo)

        new_max = 255
        new_min = 0

        for i in range(len(self.photo)):
            for j in range(len(self.photo[i])):
                for k in range(3):
                    if (self.photo[i][j][k] <= new_min):
                        self.photo[i][j][k] = 0
                    elif(self.photo[i][j][k] >= new_max):
                        self.photo[i][j][k] = 255
                    else:
                        self.photo[i][j][k] = ((self.photo[i][j][k]-im_min)*new_max)/(im_max-im_min)
        return self.photo

    def posterization(self, levels):
        myBins = np.arange(0, 255, np.round(255 / levels))

        for h in range(self.photo.shape[0]):
            for w in range(self.photo.shape[1]):
                for k in range(3):
                    current_pixel = self.photo[h][w][k]

                    # loop through bins
                    for bin in range(levels):
                        # print(myBins[bin])
                        if (current_pixel > myBins[bin]): self.photo[h][w][k] = myBins[bin]  # if inside bin assign value

                    if (current_pixel > myBins[-1]): self.photo[h][w][k] = 255

        return self.photo

    def cumsum(self, a):
        a = iter(a)
        b = [next(a)]
        for i in a:
            b.append(b[-1] + i)
        return np.array(b)

    def equalization(self, cs):
        cs_min = cs.min()
        cs_max = cs.max()

        for i in range(len(cs)):
            cs[i] = ((cs[i] - cs_min) * 255)/(cs_max - cs_min)

        for i in range(len(self.photo)):
            for j in range(len(self.photo[i])):
                for k in range(3):
                    self.photo[i][j][k] = cs[self.photo[i][j][k]]

        return self.photo

    def blur(self, ksize, border):
        k = (ksize, ksize)
        border_type = self.set_border_type(border)
        self.photo = cv2.blur(self.photo, k, borderType=border_type)
        return self.photo

    def gaussian_blur(self, kernel, stdev, border):
        border_type = self.set_border_type(border)
        self.photo = cv2.GaussianBlur(self.photo, (kernel, kernel), stdev, borderType=border_type)
        return self.photo

    def laplacian(self, kernel, border):
        ddepth = cv2.CV_8UC1
        border_type = self.set_border_type(border)
        self.photo = cv2.Laplacian(self.photo, ddepth, kernel, borderType=border_type)
        return self.photo

    def sobel(self, kernel):
        sobel_x = cv2.Sobel(self.photo, cv2.CV_8UC1, 1, 0, kernel)
        sobel_y = cv2.Sobel(self.photo, cv2.CV_8UC1, 0, 1, kernel)

        self.photo = cv2.hconcat((sobel_x, sobel_y))

        return self.photo

    def canny(self, threshold1, threshold2):
        self.photo = cv2.Canny(self.photo, threshold1, threshold2)
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_GRAY2RGB)

        return self.photo

    def mask(self, mask, border):
        mask_sharp = self.set_mask_type(mask)
        border_type = self.set_border_type(border)

        self.photo = cv2.filter2D(self.photo, cv2.CV_8UC1, mask_sharp, borderType=border_type)
        return self.photo

    def prewitt(self, mask, border):
        prewitt_mask = self.set_prewitt_mask(mask)
        border_type = self.set_border_type(border)

        self.photo = cv2.filter2D(self.photo, cv2.CV_8UC1, prewitt_mask, borderType=border_type)

        return self.photo

    def median_blur(self, mask, border):
        median_blur_mask = self.set_median_blur_mask(mask)
        border_type = self.set_border_type(border)

        self.photo = cv2.medianBlur(self.photo, median_blur_mask)

        return self.photo

    def add_images(self, second_photo):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = cv2.add(self.photo, second_photo)
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_GRAY2RGB)

        return self.photo

    def subtract_images(self, second_photo):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = cv2.subtract(self.photo, second_photo)
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_GRAY2RGB)

        return self.photo

    def set_border_type(self, border):
        if border == "Isolated":
            return cv2.BORDER_ISOLATED
        elif border == "Reflect":
            return cv2.BORDER_REFLECT
        return cv2.BORDER_REPLICATE

    def set_mask_type(self, mask):
        if mask == "[[ 0,-1, 0]\n[-1, 5,-1]\n[ 0,-1, 0]]":
            return np.array([[ 0,-1, 0],[-1, 5,-1],[ 0,-1, 0]])
        elif mask == "[[-1,-1,-1]\n[-1, 9,-1]\n[-1,-1,-1]]":
            return np.array([[-1,-1,-1],[-1, 9,-1],[-1,-1,-1]])
        return np.array([[ 1,-2, 1],[-2, 5,-2],[ 1,-2, 1]])

    def set_prewitt_mask(self, mask):
        if mask == "[[ -1, 0, 1]\n[-1, 0, 1]\tE\n[ -1, 0, 1]]":
            return np.array([[ -1, 0, 1],[-1, 0, 1],[ -1, 0, 1]])
        elif mask == "[[ -1, -1, 0]\n[-1, 0, 1]\tSE\n[ 0, 1, 1]]":
            return np.array([[ -1, -1, 0],[-1, 0, 1],[ 0, 1, 1]])
        elif mask == "[[ -1, -1, -1]\n[0, 0, 0]\tS\n[ 1, 1, 1]]":
            return np.array([[ -1, -1, -1],[0, 0, 0],[ 1, 1, 1]])
        elif mask == "[[ 0, -1, -1]\n[1, 0, -1]\tSW\n[ 1, 1, 0]]":
            return np.array([[ 0, -1, -1],[1, 0, -1],[ 1, 1, 0]])
        elif mask == "[[ 1, 0, -1]\n[1, 0, -1]\tW\n[ 1, 0, -1]]":
            return np.array([[ 1, 0, -1],[1, 0, -1],[ 1, 0, -1]])
        elif mask == "[[ 1, 1, 0]\n[1, 0, -1]\tNW\n[ 0, -1, -1]]":
            return np.array([[ 1, 1, 0],[1, 0, -1],[ 0, -1, -1]])
        elif mask == "[[ 1, 1, 1]\n[0, 0, 0]\tN\n[ -1, -1, -1]]":
            return np.array([[ 1, 1, 1],[0, 0, 0],[ -1, -1, -1]])
        return np.array([[ 0, 1, 1],[-1, 0, 1],[ -1, -1, 0]])

    def set_mask(self, mask):
        arr = np.array([[int(j) for j in i.split(' ')] for i in mask.splitlines()])
        return arr

    def set_median_blur_mask(self, mask):
        if mask == "3x3":
            return 3
        elif mask == "5x5":
            return 5
        return 7