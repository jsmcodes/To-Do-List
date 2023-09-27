from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("""
            background-color: transparent;
        """)

        widget = QWidget(self)
        widget.setStyleSheet("""
            background-color: white;
            border: 1px solid black;
            border-radius: 5px;
        """)
        self.setCentralWidget(widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()