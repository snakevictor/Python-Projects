#!/usr/bin/env python

import sys

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton

__author__ = "Victor Monteiro Ribeiro"
__version__ = "0.1b"
__maintainer__ = "Victor Monteiro Ribeiro"
__email__ = "victormribeiro.py@gmail.com"
__status__ = "Development"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic PyQt6 Window")

        # Create a label widget
        self.label = QLabel("Hello PyQt6", self)
        self.label.setGeometry(50, 50, 200, 50)  # (x, y, width, height)

        # Create a button widget
        self.button = QPushButton("Click me!", self)
        self.button.setGeometry(50, 120, 200, 50)

        # Connect the button click signal to a slot (function)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.label.setText("Button was clicked!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
