from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtCore import QSize
import sys 

class MainWindow(QMainWindow):
    title = "YouTube Downloader"

    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.title)
        self.setMaximumSize(QSize(400,300))
        self.interface()
    def interface(self):
        title = QLabel(self.title)

        url = QLabel("Ingrese la url")
        url_input = QLineEdit()
        download = QPushButton("Descargar")

        hLayout = QHBoxLayout()
        hLayout.addWidget(url)
        hLayout.addWidget(url_input)
        hLayout.addWidget(download)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addLayout(hLayout)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())