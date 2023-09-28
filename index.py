from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QLabel, QSizePolicy, \
    QDesktopWidget, QHBoxLayout
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtGui import QIcon

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.setStyleSheet("""
            * {
                font-size: 16px;
                background: rgb(230, 230, 230);
            }

            #central_widget {
                border: 1px solid black;
            }

            #window_icon_widget {
                background: rgb(204, 204, 204);
            }

            #window_icon_button {
                background: transparent;
            }

            #window_flag_widget {
                background: rgb(204, 204, 204);
            }

            #window_title_label {
                font-weight: bold;
                background: transparent;
            }

            #window_button_widget {
                background: rgb(204, 204, 204);
            }

            #window_button {
                background: transparent;
                border: none;
            }

            #window_button:hover {
                background: rgb(191, 191, 191);
            }

            #window_button:pressed {
                background: rgb(166, 166, 166);
            }

            #close_button {
                background: transparent;
                border: none;
            }

            #close_button:hover {
                background: rgb(255, 102, 102);
            }

            #close_button:pressed {
                background: rgb(255, 51, 51);
            }

            #navigation_widget {
                background: grey;
            }

            #content_widget {
                background: lightgrey;
            }
        """)
        
        screen_size = QDesktopWidget().screenGeometry().size()
        
        window_width = int(screen_size.width() * 0.75)
        window_height = int(screen_size.height() * 0.75)
        window_x = (screen_size.width() - window_width) // 2
        window_y = (screen_size.height() - window_height) // 2
        self.setGeometry(window_x, window_y, window_width, window_height)
        
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QGridLayout(self.central_widget)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setRowStretch(0, 2)
        self.main_layout.setRowStretch(1, 38)
        self.main_layout.setColumnStretch(0, 2)
        self.main_layout.setColumnStretch(1, 8)
        self.main_layout.setColumnStretch(2, 2)
        
        self.window_icon_widget = QWidget(self.central_widget)
        self.window_icon_widget.setObjectName("window_icon_widget")
        self.main_layout.addWidget(self.window_icon_widget, 0, 0)
        
        self.window_icon_layout = QHBoxLayout(self.window_icon_widget)
        self.window_icon_layout.setAlignment(Qt.AlignLeft)
        self.window_icon_layout.setSpacing(0)
        self.window_icon_layout.setContentsMargins(5, 5, 5, 5)
        
        self.window_icon_button = QPushButton(self.window_icon_widget)
        self.window_icon_button.setFixedSize(30, 30)
        self.window_icon_button.setIconSize(QSize(24, 24))
        self.window_icon_button.setIcon(QIcon("Resources/Icons/list.svg"))
        self.window_icon_button.setObjectName("window_icon_button")
        self.window_icon_layout.addWidget(self.window_icon_button)
        
        self.window_flag_widget = QWidget(self.central_widget)
        self.window_flag_widget.setObjectName("window_flag_widget")
        self.main_layout.addWidget(self.window_flag_widget, 0, 1)
        
        self.window_flag_layout = QHBoxLayout(self.window_flag_widget)
        self.window_flag_layout.setAlignment(Qt.AlignCenter)
        self.window_flag_layout.setSpacing(0)
        self.window_flag_layout.setContentsMargins(0, 0, 0, 0)
        
        self.window_title_label = QLabel("TaskMaster", self.window_flag_widget)
        self.window_title_label.setObjectName("window_title_label")
        self.window_flag_layout.addWidget(self.window_title_label)
        
        self.window_button_widget = QWidget(self.central_widget)
        self.window_button_widget.setObjectName("window_button_widget")
        self.main_layout.addWidget(self.window_button_widget, 0, 2)
        
        self.window_button_layout = QHBoxLayout(self.window_button_widget)
        self.window_button_layout.setAlignment(Qt.AlignRight)
        self.window_button_layout.setSpacing(0)
        self.window_button_layout.setContentsMargins(5, 5, 5, 5)
        
        self.minimize_button = QPushButton(self.window_button_widget)
        self.minimize_button.setObjectName("window_button")
        self.minimize_button.setFixedSize(30, 30)
        self.minimize_button.setIconSize(QSize(24, 24))
        self.minimize_button.setIcon(QIcon("Resources/Icons/minimize.svg"))
        self.minimize_button.clicked.connect(self.minimizeWindow)
        self.window_button_layout.addWidget(self.minimize_button)
        
        self.maximize_button = QPushButton(self.window_button_widget)
        self.maximize_button.setObjectName("window_button")
        self.maximize_button.setFixedSize(30, 30)
        self.maximize_button.setIconSize(QSize(24, 24))
        self.maximize_button.setIcon(QIcon("Resources/Icons/maximize.svg"))
        self.window_button_layout.addWidget(self.maximize_button)
        self.maximize_button.setEnabled(False)
        
        self.close_button = QPushButton(self.window_button_widget)
        self.close_button.setObjectName("close_button")
        self.close_button.setFixedSize(30, 30)
        self.close_button.setIconSize(QSize(24, 24))
        self.close_button.setIcon(QIcon("Resources/Icons/close.svg"))
        self.close_button.clicked.connect(QApplication.quit)
        self.window_button_layout.addWidget(self.close_button)
        
        self.navigation_widget = QWidget(self.central_widget)
        self.navigation_widget.setObjectName("navigation_widget")
        self.main_layout.addWidget(self.navigation_widget, 1, 0)
        
        self.content_widget = QWidget(self.central_widget)
        self.content_widget.setObjectName("content_widget")
        self.main_layout.addWidget(self.content_widget, 1, 1, 1, 2)
        
        self.show()
        
        self.dragging = False
        self.offset = QPoint(0, 0)
    
    def minimizeWindow(self):
        self.showMinimized()
    
    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton
              and self.window_flag_widget.geometry().contains(event.pos())
              or self.window_icon_widget.geometry().contains(event.pos())
              or self.window_button_widget.geometry().contains(event.pos())):
            self.dragging = True
            self.offset = event.globalPos() - self.pos()
    
    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPos() - self.offset)
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()