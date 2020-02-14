from PyQt5.QtWidgets import *
from main_screen import Screen

app = QApplication([])
screen = Screen()
screen.show()
app.exec_()

