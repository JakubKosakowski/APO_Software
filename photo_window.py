from hist import *
from operations import *
from Extends import *


class PhotoWindow(QWidget):
    def __init__(self, photo):
        super(PhotoWindow, self).__init__()
        self.setWindowTitle(photo)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap(photo))
        self.photo_name = photo
        self.photo = cv2.imread(self.photo_name)
        self.photo_hist = Histogram(self.photo)
        self.photo_operations = Operations(self.photo)
        self.red_hist = self.photo_hist.r_hist

        btn = QPushButton('Histogram')
        btn.clicked.connect(self.show_hist)

        neg = QPushButton('Negative')
        neg.clicked.connect(self.negative_image)

        threshold = QPushButton('Threshold')
        threshold.clicked.connect(self.threshold_extend)

        gray_threshold = QPushButton('Threshold with grayscale')
        gray_threshold.clicked.connect(self.grayscale_threshold_extend)

        binarization = QPushButton('Binarization')
        binarization.clicked.connect(self.binarization_extend)

        hist_stretching = QPushButton('Histogram stretching')
        hist_stretching.clicked.connect(self.histogram_stretching)

        posterization = QPushButton('Posterization')
        posterization.clicked.connect(self.posterization_extend)

        equalization = QPushButton('Equalization')
        equalization.clicked.connect(self.equalization_image)

        blur = QPushButton('Blur')
        blur.clicked.connect(self.kernel)

        gaussian_blur = QPushButton('Gaussian blur')
        gaussian_blur.clicked.connect(self.gaussian_values)

        laplacian = QPushButton('Laplacian')
        laplacian.clicked.connect(self.laplacian_values)

        sobel = QPushButton('Sobel')
        sobel.clicked.connect(self.sobel_values)

        canny = QPushButton('Canny')
        canny.clicked.connect(self.canny_values)

        mask_sharp = QPushButton('Mask sharp')
        mask_sharp.clicked.connect(self.mask_values)

        prewitt_mask = QPushButton('Prewitt mask')
        prewitt_mask.clicked.connect(self.prewitt_values)

        default = QPushButton('Default image')
        default.clicked.connect(self.default_image)

        user_mask = QPushButton('User mask')
        user_mask.clicked.connect(self.user_values)

        self.grid = QGridLayout(self)
        self.grid.addWidget(btn, 0, 0, Qt.AlignHCenter)
        self.grid.addWidget(neg, 0, 1, Qt.AlignHCenter)
        self.grid.addWidget(threshold, 0, 2 , Qt.AlignHCenter)
        self.grid.addWidget(gray_threshold, 0, 3, Qt.AlignHCenter)
        self.grid.addWidget(binarization, 0, 4, Qt.AlignHCenter)
        self.grid.addWidget(hist_stretching, 0, 5, Qt.AlignHCenter)
        self.grid.addWidget(posterization, 0, 6, Qt.AlignHCenter)
        self.grid.addWidget(equalization, 0, 7, Qt.AlignHCenter)
        self.grid.addWidget(self.label, 1, 1, Qt.AlignHCenter)
        self.grid.addWidget(blur, 1, 2, Qt.AlignHCenter)
        self.grid.addWidget(gaussian_blur, 1, 3, Qt.AlignHCenter)
        self.grid.addWidget(laplacian, 1, 4, Qt.AlignHCenter)
        self.grid.addWidget(sobel, 1, 5, Qt.AlignHCenter)
        self.grid.addWidget(canny, 1, 6, Qt.AlignHCenter)
        self.grid.addWidget(mask_sharp, 1, 7, Qt.AlignHCenter)
        self.grid.addWidget(prewitt_mask, 2, 2, Qt.AlignHCenter)
        self.grid.addWidget(default, 1, 0, Qt.AlignHCenter)
        self.grid.addWidget(user_mask, 2, 3, Qt.AlignHCenter)



        self.argument_one = 0
        self.argument_two = 0
        self.border_type = ""
        self.mask_type= ""

    def show_hist(self):
        self.photo_hist.show_hist()

    def negative_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.negation()
        self.save_image()

    def threshold_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.threshold(self.argument_one, self.argument_two)
        self.save_image()

    def grayscale_threshold_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.grayscale_threshold(self.argument_one)
        self.save_image()

    def binarization_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.binarization(self.argument_one)
        self.save_image()

    def histogram_stretching(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.histogram_stretching()
        self.save_image()

    def equalization_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.cumsum = self.photo_operations.cumsum(self.red_hist)
        self.photo = self.photo_operations.equalization(self.cumsum)
        self.save_image()

    def posterization_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.posterization(self.argument_one)
        self.save_image()

    def blur_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.blur(self.argument_one, self.border_type)
        self.save_image()

    def gaussian_blur_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.gaussian_blur(self.argument_one, self.argument_two, self.border_type)
        self.save_image()

    def laplacian_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.laplacian(self.argument_one, self.border_type)
        self.save_image()

    def sobel_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.sobel(self.argument_one)
        self.save_image()

    def canny_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.canny(self.argument_one, self.argument_two)
        self.save_image()

    def mask_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.mask(self.mask_type, self.border_type)
        self.save_image()

    def prewitt_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.prewitt(self.mask_type, self.border_type)
        self.save_image()

    def default_image(self):
        self.photo = cv2.imread(self.photo_name)
        self.photo_operations.set_default(self.photo)
        self.save_image()

    def user_image(self):
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2GRAY)
        self.photo = self.photo_operations.user_mask(self.mask_type, self.border_type)
        self.save_image()


    def save_image(self):
        self.photo_hist = Histogram(self.photo)
        frame = self.photo
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(str, str)
    def update_values(self, min, max):
        self.argument_one = int(min)
        self.argument_two = int(max)
        self.threshold_image()

    @pyqtSlot(str)
    def update_single_value(self, bin):
        self.argument_one = int(bin)
        self.binarization_image()

    @pyqtSlot(str)
    def update_single_value_grayscale_threshold(self, bin):
        self.argument_one = int(bin)
        self.grayscale_threshold_image()

    @pyqtSlot(str)
    def update_posterization_level(self, bin):
        self.argument_one = int(bin)
        self.posterization_image()

    @pyqtSlot(str, str)
    def update_kernel(self, bin, text):
        self.argument_one = int(bin)
        self.border_type = text
        self.blur_image()

    @pyqtSlot(str, str)
    def update_laplacian(self, bin, text):
        self.argument_one = int(bin)
        self.border_type = text
        self.laplacian_image()

    @pyqtSlot(str, str, str)
    def update_gaussian(self, kernel, stdev, border):
        self.argument_one = int(kernel)
        self.argument_two = int(stdev)
        self.border_type = border
        self.gaussian_blur_image()

    @pyqtSlot(str)
    def update_sobel(self, kernel):
        self.argument_one = int(kernel)
        self.sobel_image()

    @pyqtSlot(str, str)
    def update_canny(self, threshold1, threshold2):
        self.argument_one = int(threshold1)
        self.argument_two = int(threshold2)
        self.canny_image()

    @pyqtSlot(str, str)
    def update_mask(self, mask, border):
        self.mask_type = mask
        self.border_type = border
        self.mask_image()

    @pyqtSlot(str, str)
    def update_prewitt(self, mask, border):
        self.mask_type = mask
        self.border_type = border
        self.prewitt_image()

    @pyqtSlot(str, str)
    def update_user(self, mask, border):
        self.mask_type = mask
        self.border_type = border
        self.user_image()

    def threshold_extend(self):
        self.ui = UiExtends()
        self.ui.submitted.connect(self.update_values)
        self.ui.show()

    def binarization_extend(self):
        self.ui = Binarization()
        self.ui.submitted.connect(self.update_single_value)
        self.ui.show()

    def grayscale_threshold_extend(self):
        self.ui = Binarization()
        self.ui.submitted.connect(self.update_single_value_grayscale_threshold)
        self.ui.show()

    def posterization_extend(self):
        self.ui = Posterization()
        self.ui.submitted.connect(self.update_posterization_level)
        self.ui.show()

    def kernel(self):
       self.ui = Kernel()
       self.ui.submitted.connect(self.update_kernel)
       self.ui.show()

    def gaussian_values(self):
        self.ui = Gaussian()
        self.ui.submitted.connect(self.update_gaussian)
        self.ui.show()

    def laplacian_values(self):
        self.ui = Kernel()
        self.ui.submitted.connect(self.update_laplacian)
        self.ui.show()

    def sobel_values(self):
        self.ui = Sobel()
        self.ui.submitted.connect(self.update_sobel)
        self.ui.show()

    def canny_values(self):
        self.ui = UiExtends()
        self.ui.submitted.connect(self.update_canny)
        self.ui.show()

    def mask_values(self):
        self.ui = Mask()
        self.ui.submitted.connect(self.update_mask)
        self.ui.show()

    def prewitt_values(self):
        self.ui = Prewitt()
        self.ui.submitted.connect(self.update_prewitt)
        self.ui.show()

    def user_values(self):
        self.ui = User()
        self.ui.submitted.connect(self.update_user)
        self.ui.show()