from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog
from PySide6.QtCore import QSize
import sys 

class MainWindow(QMainWindow):
    title = "YouTube Downloader"
    qss = ""
    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.title)
        self.setMinimumSize(QSize(300,200))
        self.interface()
    def interface(self):
        title = QLabel(self.title)

        url = QLabel("Ingrese la url")
        url_input = QLineEdit()    

        hLayout = QHBoxLayout()
        hLayout.addWidget(url)
        hLayout.addWidget(url_input)
        
        bFolder = QPushButton("Seleccionar Carpeta de Salida")
        folder = QLabel("Carpeta Seleccionada: ")
        
        hLayout2 = QHBoxLayout()
        hLayout2.addWidget(bFolder)
        hLayout2.addWidget(folder)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addLayout(hLayout)
        layout.addLayout(hLayout2)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        bFolder.clicked.connect(self.select_folder)

    def select_folder(self):
        self.folder = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta", "")
        self.folderSelected.setText(f"Carpeta de Salida seleccionada: {self.folder}")
        
        
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())