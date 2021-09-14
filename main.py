from PySide6 import QtCore
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys

ui, _ = loadUiType("clone-dashboard.ui")


# run pyside6-rcc <your_resource.qrc> -o your_resource.py


class DashWindow(QMainWindow, ui):
    def __init__(self):
        super(DashWindow, self).__init__()
        # Remove default title bar
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)  # | Qt.WindowStaysOnTopHint -> put windows on top
        self.setMaximumSize(1080, 720)
        self.setWindowFlags(flags)
        self.setupUi(self)
        self.showNormal()
        self.offset = None

        self.pushButton_4.clicked.connect(self.close_win)
        self.pushButton_6.clicked.connect(self.minimize_win)
        self.pushButton_5.clicked.connect(self.mini_maximize)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def close_win(self):
        self.close()

    def mini_maximize(self):
        if self.isMaximized():
            self.pushButton_5.setIcon(QIcon("./resources/icons/maximize.svg"))
            self.showNormal()
        else:
            self.pushButton_5.setIcon(QIcon("./resources/icons/minimize.svg"))
            self.showMaximized()

    def minimize_win(self):
        self.showMinimized()


if __name__ == "__main__":
    app = QApplication()
    window = DashWindow()
    window.show()

    sys.exit(app.exec())
