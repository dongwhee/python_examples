#!/usr/bin/python
import sys

# PySide2 모듈이 설치 되어 있어야 합니다.
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (qApp, QApplication, QComboBox, QFormLayout,
    QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QSlider, QWidget, QLabel)

# items for QComboBox
items = ['apple', 'banana', 'carrot']

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize main widget
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QFormLayout(centralWidget)

        # QLineEdit example
        textLayout = QHBoxLayout()
        self.text = QLineEdit('Hello, PySide2')
        self.text.setClearButtonEnabled(True)
        textLayout.addWidget(self.text)
        self.btn = QPushButton('Say')
        textLayout.addWidget(self.btn)
        self.text.returnPressed.connect(self.btn.animateClick)
        self.btn.clicked.connect(self.say)
        layout.addRow('Text:', textLayout)

        # QComboBox example
        self.combo = QComboBox()
        self.combo.addItems(items)
        layout.addRow('Item:', self.combo)
        self.combo.currentIndexChanged.connect(self.selected)

        # QSlide example
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(100)
        self.slider.valueChanged.connect(self.slide)
        layout.addRow('Volume:', self.slider)

        # QLabel example
        self.label = QLabel()
        self.label.setText('')
        layout.addRow('Result:', self.label)

    # button event handler
    def say(self):
        text = self.text.text()
        self.label.setText(text)

    # combobox event handler
    def selected(self, index):
        self.label.setText(items[index])

    # slider event handler
    def slide(self, value):
        self.label.setText(str(value))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    # wait for gui terminated
    sys.exit(app.exec_())
