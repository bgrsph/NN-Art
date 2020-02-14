import subprocess
import time
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import *

args = {}

class Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ARTIFICIAL BUT INTELLIGENT ART BY BUĞRA SİPAHİOĞLU')
        sizeObject = QDesktopWidget().screenGeometry(-1)
        print(" Screen size : " + str(sizeObject.height()) + "x" + str(sizeObject.width()))
        oImage = QImage("ui_images/background-5.png")
        sImage = oImage.scaled(QSize(sizeObject.width(), sizeObject.height()))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.selectContentImageButton = QPushButton('SELECT CONTENT IMAGE', self)
        self.selectContentImageButton.setFont(QFont('Courier', 18))
        self.selectContentImageButton.move(0, 0)
        self.selectContentImageButton.setMinimumSize(400,400)
        self.selectContentImageButton.clicked.connect(self.selectContentButtonPressed)
        self.selectContentImageButton.setStyleSheet("border-image:url(ui_images/background-3.png); color: white")

        self.IterationLabel = QLabel("ITERATIONS: ", self)
        self.IterationLabel.setText("<font color='white'>ITERATIONS</font>");
        self.IterationLabel.setFont(QFont('Courier'))
        self.IterationLabel.setStyleSheet("background-color: None")
        self.IterationLabel.setMinimumSize(200, 50)
        self.IterationLabel.move(20, 400)

        self.iterationsLineEdit = QLineEdit(self)
        self.iterationsLineEdit.setStyleSheet("border-image: url(ui_images/background-3.png); color:white")
        self.iterationsLineEdit.setText("250")
        self.iterationsLineEdit.setFont(QFont('Courier'))
        self.iterationsLineEdit.move(130, 415)

        self.learningRateLabel = QLabel("LEARNING RATE: ", self)
        self.learningRateLabel.setText("<font color='white'>LEARNING RATE</font>");
        self.learningRateLabel.setStyleSheet("background-color: None")
        self.learningRateLabel.move(20, 430)
        self.learningRateLabel.setFont(QFont('Courier'))
        self.learningRateLabel.setMinimumSize(200, 50)

        self.learningRateLineEdit = QLineEdit(self)
        self.learningRateLineEdit.setStyleSheet("border-image: url(ui_images/background-3.png); color:white")
        self.learningRateLineEdit.setText("0.1")
        self.learningRateLineEdit.setFont(QFont('Courier'))
        self.learningRateLineEdit.move(130, 445)

        self.outputLabel = QLabel("ARTWORK NAME: ", self)
        self.outputLabel.setText("<font color='white'>ARTWORK NAME</font>");
        self.outputLabel.setStyleSheet("background-color: None")
        self.outputLabel.move(20, 460)
        self.outputLabel.setFont(QFont('Courier'))
        self.outputLabel.setMinimumSize(200, 50)

        self.outputLineEdit = QLineEdit(self)
        self.outputLineEdit.setStyleSheet("border-image: url(ui_images/background-3.png); color:white")
        self.outputLineEdit.setText("My-Artwork")
        self.outputLineEdit.setFont(QFont('Courier'))
        self.outputLineEdit.move(130, 475)

        self.selectStyleImageButton = QPushButton('SELECT STYLE IMAGE', self)
        self.selectStyleImageButton.move(0, 500)
        self.selectStyleImageButton.setMinimumSize(400,400)
        self.selectStyleImageButton.clicked.connect(self.selectStyleButtonPressed)
        self.selectStyleImageButton.setFont(QFont('Courier', 18))
        self.selectStyleImageButton.setStyleSheet("border-image:url(ui_images/background-3.png); color: white")

        self.createArtWorkButton = QPushButton('START TRANSFER', self)
        self.createArtWorkButton.move(500, 400)
        self.createArtWorkButton.setMinimumSize(300, 100)
        self.createArtWorkButton.clicked.connect(self.createArtWorkButtonPressed)
        self.createArtWorkButton.setFont(QFont('Courier', 18))
        self.createArtWorkButton.setStyleSheet("border-image:url(ui_images/background-3.png); color: white")

        self.artworkPictureButton = QPushButton(self)
        self.artworkPictureButton.move(850, 50)
        self.artworkPictureButton.setMinimumSize(500, 800)
        #self.artworkPictureButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.artworkPictureButton.setStyleSheet("border-image:url(ui_images/background-3.png);")

        self.showFullScreen()


    def selectContentButtonPressed(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "Image files (*.jpg *.jpeg *.png)")
        args["content_path"] = fname
        self.selectContentImageButton.setStyleSheet("border-image:url(" + fname[0] + "); color: white")
        self.selectContentImageButton.setText("")


    def selectStyleButtonPressed(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "Image files (*.jpg *.jpeg *.png)")
        args["style_path"] = fname
        self.selectStyleImageButton.setStyleSheet("border-image:url(" + fname[0] + "); color: white")
        self.selectStyleImageButton.setText("")

    def createArtWorkButtonPressed(self):
        self.createArtWorkButton.setText("Creating Artwork...")
        time.sleep(2)
        content_image_path = args['content_path'][0]
        style_image_path = args['style_path'][0]
        iterations = self.iterationsLineEdit.text()
        output = self.outputLineEdit.text() + ".jpg"
        pass_arg = []
        pass_arg.append("/Users/bugrasipahioglu/repos/neural-style/run_script.sh")
        pass_arg.append(content_image_path)
        pass_arg.append(style_image_path)
        pass_arg.append(output)
        pass_arg.append(iterations)
        subprocess.check_call(pass_arg)
        self.artworkPictureButton.setIcon(QIcon(output))
        self.artworkPictureButton.setIconSize(self.artworkPictureButton.size())
        self.createArtWorkButton.setText("Artwork is Ready")