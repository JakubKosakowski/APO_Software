import cv2
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import numpy as np


class Histogram(QWidget):
    def __init__(self, photo=None):
        super().__init__()
        self.photo = photo.copy()
        self.set_hist(self.photo)
        self.tab = None

    def show_hist(self):
        rng = list(range(0, 256))
        plt.bar(rng, self.b_hist, color='b')
        plt.bar(rng, self.g_hist, color='g')
        plt.bar(rng, self.r_hist, color='r')
        plt.show()
        self.show_table()

    def set_hist(self, photo):
        b, g, r = cv2.split(photo)
        self.b_hist = self.count_hist(b)
        self.g_hist = self.count_hist(g)
        self.r_hist = self.count_hist(r)


    def count_hist(self, col: list):
        result = [0] * 256
        image_array = np.hstack(col)
        for value in image_array:
            result[value] += 1
        return result

    def show_table(self):
        if self.tab is None:
            self.tab = TableHistogram(self.photo)
        self.tab.show()


class TableHistogram(Histogram, QWidget):
    def __init__(self, photo):
        super().__init__(photo)
        self.title = 'Table Histogram'
        self.setWindowTitle(self.title)
        self.create_table()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table_widget)
        self.setLayout(self.layout)

    def create_table(self):
        self.table_widget = QTableWidget()

        self.table_widget.setRowCount(4)
        self.table_widget.setColumnCount(257)

        self.table_widget.setItem(1, 0, QTableWidgetItem("RED"))
        self.table_widget.setItem(2, 0, QTableWidgetItem("GREEN"))
        self.table_widget.setItem(3, 0, QTableWidgetItem("BLUE"))
        for i in range(1, 257):
            self.table_widget.setItem(0, i, QTableWidgetItem(str(i-1)))
            self.table_widget.setItem(1, i, QTableWidgetItem(str(self.r_hist[i - 1])))
            self.table_widget.setItem(2, i, QTableWidgetItem(str(self.g_hist[i - 1])))
            self.table_widget.setItem(3, i, QTableWidgetItem(str(self.b_hist[i - 1])))

        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)