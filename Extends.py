from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class UiExtends(QWidget):
    submitted = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Threshold extend")
        self.setFixedWidth(200)
        self.setFixedHeight(200)
        self.min_text = QLabel()
        self.min_text.move(10, 20)
        self.min_text.setText("Insert min value")

        self.max_text = QLabel()
        self.max_text.move(30, 20)
        self.max_text.setText("Insert max value")

        self.min_value = QLineEdit()
        self.min_value.resize(80, 5)
        self.min_value.move(15, 20)
        self.min_value.insert("0")

        self.max_value = QLineEdit()
        self.max_value.resize(80, 5)
        self.max_value.move(40, 20)
        self.max_value.insert("0")

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_values)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.min_text, 0, 0)
        self.vbox.addWidget(self.min_value, 1, 0)
        self.vbox.addWidget(self.max_text, 2, 0)
        self.vbox.addWidget(self.max_value, 3, 0)
        self.vbox.addWidget(self.btn, 4, 0)

        self.vbox.setRowStretch(5, 1)

    def send_values(self):
        self.submitted.emit(
            self.min_value.text(),
            self.max_value.text()
        )
        self.close()


class Binarization(QWidget):
    submitted = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Binarization extend")
        self.setFixedWidth(200)
        self.setFixedHeight(200)
        self.threshold_text = QLabel()
        self.threshold_text.move(10, 20)
        self.threshold_text.setText("Insert binarization threshold:")

        self.threshold_value = QLineEdit()
        self.threshold_value.resize(80, 5)
        self.threshold_value.move(15, 20)
        self.threshold_value.insert("0")

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_values)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.threshold_text, 0, 0)
        self.vbox.addWidget(self.threshold_value, 1, 0)
        self.vbox.addWidget(self.btn, 2, 0)

        self.vbox.setRowStretch(3, 1)

    def send_values(self):
        self.submitted.emit(
            self.threshold_value.text()
        )
        self.close()

class Posterization(QWidget):
    submitted = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Binarization extend")
        self.setFixedWidth(200)
        self.setFixedHeight(200)
        self.posterization_text = QLabel()
        self.posterization_text.move(10, 20)
        self.posterization_text.setText("Insert posterization levels:")

        self.posterization_value = QLineEdit()
        self.posterization_value.resize(80, 5)
        self.posterization_value.move(15, 20)
        self.posterization_value.insert("1")

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_values)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.posterization_text, 0, 0)
        self.vbox.addWidget(self.posterization_value, 1, 0)
        self.vbox.addWidget(self.btn, 2, 0)

        self.vbox.setRowStretch(3, 1)

    def send_values(self):
        self.submitted.emit(
            self.posterization_value.text()
        )
        self.close()


class Kernel(QWidget):
    submitted = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kernel size")
        self.kernel_text = QLabel()
        self.kernel_text.move(10, 20)
        self.kernel_text.setText("Insert kernel value:")

        self.kernel_value = QLineEdit()
        self.kernel_value.resize(80, 5)
        self.kernel_value.move(15, 20)
        self.kernel_value.insert("1")

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_values)

        self.list = QListWidget()
        self.list.setGeometry(50, 70, 150, 60)
        self.border_type = "Isolated"
        self.list.addItem("Isolated")
        self.list.addItem("Reflect")
        self.list.addItem("Replicate")
        self.list.itemClicked.connect(self.clicked)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.kernel_text, 0, 0)
        self.vbox.addWidget(self.kernel_value, 1, 0)
        self.vbox.addWidget(self.list, 0, 1)
        self.vbox.addWidget(self.btn, 2, 0)

        self.vbox.setRowStretch(3, 1)

    def send_values(self):
        self.submitted.emit(
            self.kernel_value.text(),
            self.border_type
        )
        self.close()

    def clicked(self, item):
        self.border_type = item.text()

class Gaussian(QWidget):
    submitted = pyqtSignal(str, str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gaussian values")
        self.kernel_text = QLabel()
        self.kernel_text.move(10, 20)
        self.kernel_text.setText("Insert kernel size")

        self.stdev_text = QLabel()
        self.stdev_text.move(30, 20)
        self.stdev_text.setText("Insert standard deviation")

        self.kernel_value = QLineEdit()
        self.kernel_value.resize(80, 5)
        self.kernel_value.move(15, 20)
        self.kernel_value.insert("0")

        self.stdev_value = QLineEdit()
        self.stdev_value.resize(80, 5)
        self.stdev_value.move(40, 20)
        self.stdev_value.insert("0")

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_values)

        self.list = QListWidget()
        self.list.setGeometry(50, 70, 150, 60)
        self.border_type = "Isolated"
        self.list.addItem("Isolated")
        self.list.addItem("Reflect")
        self.list.addItem("Replicate")
        self.list.itemClicked.connect(self.clicked)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.kernel_text, 0, 0)
        self.vbox.addWidget(self.kernel_value, 1, 0)
        self.vbox.addWidget(self.stdev_text, 2, 0)
        self.vbox.addWidget(self.stdev_value, 3, 0)
        self.vbox.addWidget(self.btn, 4, 0)
        self.vbox.addWidget(self.list, 0, 1)

        self.vbox.setRowStretch(5, 1)

    def send_values(self):
        self.submitted.emit(
            self.kernel_value.text(),
            self.stdev_value.text(),
            self.border_type
        )
        self.close()

    def clicked(self, item):
        self.border_type = item.text()

class Sobel(QWidget):
    submitted = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sobel kernel")
        self.setFixedWidth(200)
        self.setFixedHeight(200)
        self.kernel_text = QLabel()
        self.kernel_text.move(10, 20)
        self.kernel_text.setText("Insert Sobel kernel size:")

        self.kernel_value = QLineEdit()
        self.kernel_value.resize(80, 5)
        self.kernel_value.move(15, 20)
        self.kernel_value.insert("1")

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_values)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.kernel_text, 0, 0)
        self.vbox.addWidget(self.kernel_value, 1, 0)
        self.vbox.addWidget(self.btn, 2, 0)

        self.vbox.setRowStretch(3, 1)

    def send_values(self):
        self.submitted.emit(
            self.kernel_value.text()
        )
        self.close()


class Mask(QWidget):
    submitted = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sharp mask")
        self.mask_text = QLabel()
        self.mask_text.setText("Select sharp mask: ")

        self.border_text = QLabel()
        self.border_text.setText("Select border type: ")

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_values)

        self.list = QListWidget()
        self.list.setGeometry(50, 70, 150, 60)
        self.mask_type = "[[ 0,-1, 0]\n[-1, 5,-1]\n[ 0,-1, 0]]"
        self.list.addItem("[[ 0,-1, 0]\n[-1, 5,-1]\n[ 0,-1, 0]]")
        self.list.addItem("[[-1,-1,-1]\n[-1, 9,-1]\n[-1,-1,-1]]")
        self.list.addItem("[[ 1,-2, 1]\n[-2, 5,-2]\n[ 1,-2, 1]]")
        self.list.itemClicked.connect(self.clicked)

        self.border = QListWidget()
        self.border.setGeometry(50, 70, 150, 60)
        self.border_type = "Isolated"
        self.border.addItem("Isolated")
        self.border.addItem("Reflect")
        self.border.addItem("Replicate")
        self.border.itemClicked.connect(self.clicked_border)


        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.mask_text, 0, 0)
        self.vbox.addWidget(self.list, 0, 1)
        self.vbox.addWidget(self.border_text, 0, 2)
        self.vbox.addWidget(self.border, 0, 3)
        self.vbox.addWidget(self.btn, 0, 4)

        self.vbox.setRowStretch(5, 1)

    def send_values(self):
        self.submitted.emit(
            self.mask_type,
            self.border_type
        )
        self.close()

    def clicked(self, item):
        self.mask_type = item.text()

    def clicked_border(self, item):
        self.border_type = item.text()


class Prewitt(QWidget):
    submitted = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prewitt values")
        self.prewitt_text = QLabel()
        self.prewitt_text.setText("Select Prewitt mask: ")

        self.border_text = QLabel()
        self.border_text.setText("Select border type: ")

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_values)

        self.list = QListWidget()
        self.list.setGeometry(50, 70, 150, 60)
        self.prewitt_type = "[[ -1, 0, 1]\n[-1, 0, 1]\tE\n[ -1, 0, 1]]"
        self.list.addItem("[[ -1, 0, 1]\n[-1, 0, 1]\tE\n[ -1, 0, 1]]")
        self.list.addItem("[[ -1, -1, 0]\n[-1, 0, 1]\tSE\n[ 0, 1, 1]]")
        self.list.addItem("[[ -1, -1, -1]\n[0, 0, 0]\tS\n[ 1, 1, 1]]")
        self.list.addItem("[[ 0, -1, -1]\n[1, 0, -1]\tSW\n[ 1, 1, 0]]")
        self.list.addItem("[[ 1, 0, -1]\n[1, 0, -1]\tW\n[ 1, 0, -1]]")
        self.list.addItem("[[ 1, 1, 0]\n[1, 0, -1]\tNW\n[ 0, -1, -1]]")
        self.list.addItem("[[ 1, 1, 1]\n[0, 0, 0]\tN\n[ -1, -1, -1]]")
        self.list.addItem("[[ 0, 1, 1]\n[-1, 0, 1]\tNE\n[ -1, -1, 0]]")
        self.list.itemClicked.connect(self.clicked)

        self.border = QListWidget()
        self.border.setGeometry(50, 70, 150, 60)
        self.border_type = "Isolated"
        self.border.addItem("Isolated")
        self.border.addItem("Reflect")
        self.border.addItem("Replicate")
        self.border.itemClicked.connect(self.clicked_border)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.prewitt_text, 0, 0)
        self.vbox.addWidget(self.list, 0, 1)
        self.vbox.addWidget(self.border_text, 0, 2)
        self.vbox.addWidget(self.border, 0, 3)
        self.vbox.addWidget(self.btn, 0, 4)

        self.vbox.setRowStretch(5, 1)

    def send_values(self):
        self.submitted.emit(
            self.prewitt_type,
            self.border_type
        )
        self.close()

    def clicked(self, item):
        self.prewitt_type = item.text()

    def clicked_border(self, item):
        self.border_type = item.text()

class User(QWidget):
    submitted = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("User mask")
        self.mask_text = QLabel()
        self.mask_text.setText("Write user mask: ")

        self.border_text = QLabel()
        self.border_text.setText("Select border type: ")

        self.mask_value = QPlainTextEdit(self)
        self.mask_value.setFixedHeight(150)
        self.mask_value.insertPlainText("0 0 0\n0 0 0\n0 0 0")

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_values)

        self.border = QListWidget()
        self.border.setGeometry(50, 70, 150, 60)
        self.border_type = "Isolated"
        self.border.addItem("Isolated")
        self.border.addItem("Reflect")
        self.border.addItem("Replicate")
        self.border.itemClicked.connect(self.clicked_border)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.mask_text, 0, 0)
        self.vbox.addWidget(self.mask_value, 0, 1)
        self.vbox.addWidget(self.border_text, 0, 2)
        self.vbox.addWidget(self.border, 0, 3)
        self.vbox.addWidget(self.btn, 0, 4)

        self.vbox.setRowStretch(5, 1)


    def send_values(self):
        self.submitted.emit(
            self.mask_value.toPlainText(),
            self.border_type
        )
        self.close()

    def clicked_border(self, item):
        self.border_type = item.text()


class Median(QWidget):
    submitted = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("User mask")
        self.mask_text = QLabel()
        self.mask_text.setText("Select median blur mask: ")

        self.border_text = QLabel()
        self.border_text.setText("Select border type: ")

        self.mask_list = QListWidget()
        self.mask_list.setGeometry(50, 70, 150, 60)
        self.mask_value = "3x3"
        self.mask_list.addItem("3x3")
        self.mask_list.addItem("5x5")
        self.mask_list.addItem("7x7")
        self.mask_list.itemClicked.connect(self.clicked_mask)

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_values)

        self.border = QListWidget()
        self.border.setGeometry(50, 70, 150, 60)
        self.border_type = "Isolated"
        self.border.addItem("Isolated")
        self.border.addItem("Reflect")
        self.border.addItem("Replicate")
        self.border.itemClicked.connect(self.clicked_border)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.mask_text, 0, 0)
        self.vbox.addWidget(self.mask_list, 0, 1)
        self.vbox.addWidget(self.border_text, 0, 2)
        self.vbox.addWidget(self.border, 0, 3)
        self.vbox.addWidget(self.btn, 0, 4)

        self.vbox.setRowStretch(5, 1)

    def send_values(self):
        self.submitted.emit(
            self.mask_value,
            self.border_type
        )
        self.close()

    def clicked_border(self, item):
        self.border_type = item.text()

    def clicked_mask(self, item):
        self.mask_value = item.text()


class Blending(QWidget):
    submitted = pyqtSignal(str, str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blending values")
        self.setFixedWidth(200)
        self.setFixedHeight(200)
        self.alpha_text = QLabel()
        self.alpha_text.move(10, 20)
        self.alpha_text.setText("Insert alpha values:")

        self.alpha_value = QLineEdit()
        self.alpha_value.resize(80, 5)
        self.alpha_value.insert("0.1")

        self.beta_text = QLabel()
        self.beta_text.move(10, 20)
        self.beta_text.setText("Insert beta values:")

        self.beta_value = QLineEdit()
        self.beta_value.resize(80, 5)
        self.beta_value.insert("0.1")

        self.gamma_text = QLabel()
        self.gamma_text.move(10, 20)
        self.gamma_text.setText("Insert gamma values:")

        self.gamma_value = QLineEdit()
        self.gamma_value.resize(80, 5)
        self.gamma_value.insert("0")

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_values)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.alpha_text, 0, 0)
        self.vbox.addWidget(self.alpha_value, 1, 0)
        self.vbox.addWidget(self.beta_text, 2, 0)
        self.vbox.addWidget(self.beta_value, 3, 0)
        self.vbox.addWidget(self.gamma_text, 4, 0)
        self.vbox.addWidget(self.gamma_value, 5, 0)
        self.vbox.addWidget(self.btn, 6, 0)

        self.vbox.setRowStretch(7, 1)

    def send_values(self):
        self.submitted.emit(
            self.alpha_value.text(),
            self.beta_value.text(),
            self.gamma_value.text()
        )
        self.close()

class Logic(QWidget):
    submitted = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blending values")
        self.setFixedWidth(200)
        self.setFixedHeight(200)
        self.operation_text = QLabel()
        self.operation_text.move(10, 20)
        self.operation_text.setText("Select operation type:")

        self.operation = QListWidget()
        self.operation.setGeometry(50, 70, 150, 60)
        self.operation_type = "NOT"
        self.operation.addItem("NOT")
        self.operation.addItem("AND")
        self.operation.addItem("OR")
        self.operation.addItem("XOR")
        self.operation.itemClicked.connect(self.clicked_operation)

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_values)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.operation_text, 0, 0)
        self.vbox.addWidget(self.operation, 1, 0)
        self.vbox.addWidget(self.btn, 2, 0)

        self.vbox.setRowStretch(3, 1)

    def send_values(self):
        self.submitted.emit(
            self.operation_type
        )
        self.close()

    def clicked_operation(self, item):
        self.operation_type = item.text()


class Morphology(QWidget):
    submitted = pyqtSignal(str, str, str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blending values")
        self.setFixedWidth(400)
        self.setFixedHeight(400)
        self.operation_text = QLabel()
        self.operation_text.move(10, 20)
        self.operation_text.setText("Select operation type:")

        self.iteration_text = QLabel()
        self.iteration_text.move(10, 20)
        self.iteration_text.setText("Write amount of iterations(Only ERODE and DILATE):")

        self.iteration_value = QLineEdit()
        self.iteration_value.resize(80, 5)
        self.iteration_value.insert("1")

        self.element_text = QLabel()
        self.element_text.move(10, 20)
        self.element_text.setText("Select structure element:")

        self.border_text = QLabel()
        self.border_text.move(10, 20)
        self.border_text.setText("Select border type:")

        self.operation = QListWidget()
        self.operation.setGeometry(50, 70, 150, 60)
        self.operation_type = "OPEN"
        self.operation.addItem("ERODE")
        self.operation.addItem("DILATE")
        self.operation.addItem("OPEN")
        self.operation.addItem("CLOSE")
        self.operation.itemClicked.connect(self.clicked_operation)

        self.element = QListWidget()
        self.element.setGeometry(50, 70, 150, 60)
        self.element_type = "DIAMOND(4x4)"
        self.element.addItem("DIAMOND(4x4)")
        self.element.addItem("SQUARE(8x8)")
        self.element.itemClicked.connect(self.clicked_element)

        self.border = QListWidget()
        self.border.setGeometry(50, 70, 150, 60)
        self.border_type = "Isolated"
        self.border.addItem("Isolated")
        self.border.addItem("Reflect")
        self.border.addItem("Replicate")
        self.border.itemClicked.connect(self.clicked_border)

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_values)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.operation_text, 0, 0)
        self.vbox.addWidget(self.operation, 1, 0)
        self.vbox.addWidget(self.element_text, 2, 0)
        self.vbox.addWidget(self.element, 3, 0)
        self.vbox.addWidget(self.border_text, 4, 0)
        self.vbox.addWidget(self.border, 5, 0)
        self.vbox.addWidget(self.iteration_text, 6, 0)
        self.vbox.addWidget(self.iteration_value, 7, 0)
        self.vbox.addWidget(self.btn, 8, 0)

        self.vbox.setRowStretch(9, 1)

    def send_values(self):
        self.submitted.emit(
            self.operation_type,
            self.element_type,
            self.border_type,
            self.iteration_value.text()
        )
        self.close()

    def clicked_operation(self, item):
        self.operation_type = item.text()

    def clicked_element(self, item):
        self.element_type = item.text()

    def clicked_border(self, item):
        self.border_type = item.text()