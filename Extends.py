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