import sys

import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from photo_window import *

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("APO Jakub Kosakowski : Image project")
        self.setFixedWidth(500)
        self.setFixedHeight(50)
        btn = QPushButton('Browse')
        btn.clicked.connect(self.open_image)
        grid = QGridLayout(self)
        grid.addWidget(btn, 0, 0, Qt.AlignHCenter)
        self.popups = []

    def add_new_window(self, photo):
        self.window = PhotoWindow(photo)
        self.popups.append(self.window)
        self.window.show()

    def open_image(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(
                                                      self, 'Select Photo',
                                                      QDir.currentPath(),
                                                      'Images (*.png *.jpg *.gif *.bmp)')
            if not filename:
                return
        self.add_new_window(filename)

    def closeEvent(self, event):
        QApplication.closeAllWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())