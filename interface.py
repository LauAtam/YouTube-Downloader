from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog
from PySide6.QtCore import QSize
from main import download
import sys 

class MainWindow(QMainWindow):
    title = "YouTube Downloader"
    qss = ""
    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.title)
        self.setStyleSheet(self.qss)
        self.setMinimumSize(QSize(300,200))
        self.interface()
    def interface(self):
        title = QLabel(self.title)

        url = QLabel("Ingrese la url")
        self.url_input = QLineEdit()    

        hLayout = QHBoxLayout()
        hLayout.addWidget(url)
        hLayout.addWidget(self.url_input)
        
        bFolder = QPushButton("Seleccionar Carpeta de Salida")
        self.folderSelected = QLabel("Carpeta seleccionada: ")
        
        

        bDownloadVideo = QPushButton("Descargar Video")
        bDownloadAudio = QPushButton("Descargar Audio")

        hLayoutD = QHBoxLayout()
        hLayoutD.addWidget(bDownloadVideo)
        hLayoutD.addWidget(bDownloadAudio)

        footer = QLabel()
        
        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addLayout(hLayout)
        layout.addWidget(bFolder)
        layout.addWidget(self.folderSelected)
        layout.addLayout(hLayoutD)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        bFolder.clicked.connect(self.select_folder)
        bDownloadVideo.clicked.connect(self.downloadVideo)
    def select_folder(self):
        self.folder = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta", "")
        self.folderSelected.setText(f"Carpeta Seleccionada: \n {self.folder}")
    
    def downloadVideo(self):
        if self.folder != '' and self.url_input.text() != '' :
            download(self.url_input.text(), self.folder)
        else: 
            pass
    
    #audio    
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())