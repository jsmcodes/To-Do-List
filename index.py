from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QSizePolicy, QDesktopWidget
from PyQt5.QtCore import Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("""
            border-radius: 5px;
            background-color: transparent;
        """)

        screen_size = QDesktopWidget().screenGeometry().size()

        window_width = int(screen_size.width() * 0.75)
        window_height = int(screen_size.height() * 0.75)

        window_x = (screen_size.width() - window_width) // 2
        window_y = (screen_size.height() - window_height) // 2

        self.setGeometry(window_x, window_y, window_width, window_height)

        widget = QWidget(self)
        widget.setStyleSheet("""
            background-color: rgba(204, 204, 204, 1.0);
            border: 1px solid black;
            border-radius: 5px;
        """)
        self.setCentralWidget(widget)

        main_layout = QGridLayout(widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()