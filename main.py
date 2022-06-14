import time
import PIL.Image
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtGui
from PyQt5 import QtWidgets as Q
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import matplotlib.image as mpimg


# GUI window
app = QApplication([])
window = QMainWindow()
window.setStyleSheet("background-color: rgba(165, 241, 246, 0.3);")
window.setAnimated(True)

# Image Label
label = QLabel(window)
label.setAlignment(Qt.AlignCenter)
filename = QFileDialog.getOpenFileName(window, 'Open Image File', "", "Image files (*.jpg *.jpeg *.png)")
fileimg = filename[0]
fileimg = fileimg.replace("/", "\\")
image = Image.open(fileimg)


# Image Info Label
info = QLabel(window)
info.setGeometry(0, 480, 170, 120)
info.setStyleSheet("background-color: rgba(165, 241, 246, 0.1); border-radius: 15px;")
info.setFont(QFont("Arial", 10))
info.setText(" Image Info:" +
              "\n     Width: " + str(image.size[0]) +
              "\n     Height: " + str(image.size[1]) +
              "\n     Format: " + str(image.format) +
              "\n     Mode: " + str(image.mode))
info.hide()


def get_img_file():
    image = QPixmap(fileimg)
    label.setPixmap(image)
    label.setScaledContents(True)
    label.setGeometry(320, 150, 1280, 720)
    info.show()
    label.show()


# Slider for measure
Sd = QSlider(Qt.Horizontal, window)
Sd.setRange(-1000, 1000)
Sd.setGeometry(600, 950, 700, 10)
Sd.setStyleSheet("QSlider::groove:horizontal ""{"
                 "border:none;"
                 "background-color: rgba(165, 241, 246, 0.2);"
                 "position: absolute;" "}"
                 "QSlider::handle" "{"
                 "height: 10px; width:10px; border-radius:1px;"
                 "background: #000000; border: 0.5px solid #000000"
                 "}")
slider = window.findChild(QSlider, "horizontalSlider")
sliderval = QLabel(window)
sliderval.setGeometry(930, 890, 40, 40)
sliderval.setStyleSheet(
        'border-radius:10; background-color: rgba(255, 255, 255, 0.2); color: rgba(0,0,0,0.7); ')
sliderval.setFont(QFont('Tw Cen MT (Headings)', 10))


def slidenum(value):
    sliderval.setNum(Sd.value()/100)
    pass


Sd.valueChanged.connect(slidenum)
sliderval.show()

# Label
l0 = QLabel(window)
l0.setGeometry(5, 45, 165, 30)
l0.setFont(QFont('Tw Cen MT (Headings)', 12))
l0.setText("  X    Y    W     H")
# Text box
tbox = QPlainTextEdit(window)
tbox.setGeometry(660, 2, 600, 38)
tbox.setStyleSheet(
    'border-radius:5 ; background-color: #1b2626; color: rgba(255,255,255,0.7); border: 0.5px solid #87909A;')
tbox.setFont(QFont('Tw Cen MT (Headings)', 12))

# Posx int box
tbox1 = QLineEdit(window)
tbox1.setGeometry(5, 80, 35, 35)
tbox1.setStyleSheet(
    'border-radius:5 ; background-color: #1b2626; color: rgba(255,255,255,0.7); border: 0.5px solid #87909A;')
tbox1.setFont(QFont('Tw Cen MT (Headings)', 12))

# Posy int box
tbox2 = QLineEdit(window)
tbox2.setGeometry(45, 80, 35, 35)
tbox2.setStyleSheet(
    'border-radius:5 ; background-color: #1b2626; color: rgba(255,255,255,0.7); border: 0.5px solid #87909A;')
tbox2.setFont(QFont('Tw Cen MT (Headings)', 12))

# Width int box
tbox3 = QLineEdit(window)
tbox3.setGeometry(85, 80, 35, 35)
tbox3.setStyleSheet(
    'border-radius:5 ; background-color: #1b2626; color: rgba(255,255,255,0.7); border: 0.5px solid #87909A;')
tbox3.setFont(QFont('Tw Cen MT (Headings)', 12))

# Height int box
tbox4 = QLineEdit(window)
tbox4.setGeometry(125, 80, 35, 35)
tbox4.setStyleSheet(
    'border-radius:5 ; background-color: #1b2626; color: rgba(255,255,255,0.7); border: 0.5px solid #87909A;')
tbox4.setFont(QFont('Tw Cen MT (Headings)', 12))



# Dialer
dial = QDial(window)
dial.setGeometry(1810, 880, 100, 100)
dial.setStyleSheet(
                 "background-color: rgba(165, 241, 246, 0.2);")

dialval = QLabel(window)
dialval.setGeometry(1838, 830, 40, 40)
dialval.setStyleSheet(
        'border-radius:10; background-color: rgba(255, 255, 255, 0.2); color: rgba(0,0,0,0.7); ')
dialval.setFont(QFont('Tw Cen MT (Headings)', 10))

dial.setRange(0, 359)
dial.setValue(0)
dial.setNotchTarget(1)
dial.setNotchesVisible(True)


def dialmoved(value):
    value = dial.value()
    dialval.setText(str(value))
    pass


dial.valueChanged.connect(dialmoved)
dialval.show()


# Cropping
def crop():
    image2 = image.copy()
    (left, upper, right, lower) = (int(tbox1.text()), int(tbox2.text()), int(tbox3.text()), int(tbox4.text()))
    cimg = image2.crop((left, upper, right, lower))
    plt.imshow(cimg)
    plt.show()


# TO FLIP FROM top to bottom,left to right,rotate 90,rotate 180,rotate 270
def TtoB():
    tFL = image.transpose(Image.FLIP_TOP_BOTTOM)
    plt.imshow(tFL)
    plt.show()


def RtoL():
    tFL1 = image.transpose(Image.FLIP_LEFT_RIGHT)
    plt.imshow(tFL1)
    plt.show()


# Resizing
def resize():
    newsize = (int(tbox3.text()), int(tbox4.text()))
    imgresize = image.resize(newsize, Image.LANCZOS)
    plt.imshow(imgresize)
    plt.show()


# Rotate
def rotate():
     angle = dial.value()
     Rimg = image.rotate(angle)
     plt.imshow(Rimg)
     plt.show()


# Watermark
def watermark():
    wimg = image.copy()
    draw = ImageDraw.Draw(wimg)
    font = ImageFont.truetype("arial.ttf", 100)
# text(pos,text,fill color,font)
    draw.text((int(tbox1.text()), int(tbox2.text())), tbox.toPlainText(), (255, 255, 255), font=font)
    plt.imshow(wimg)
    plt.show()


# Image watermark
def imagewater():
     filename1 = QFileDialog.getOpenFileName(window, 'Open Image File', "", "Image files (*.jpg *.jpeg *.png)")
     fileimg1 = filename1[0]
     fileimg1 = fileimg1.replace("/", "\\")
     image56 = Image.open(fileimg1)
     size_of_watermark = (int(tbox3.text()), int(tbox4.text()))
     waterimg = image56.copy()
     waterimg.thumbnail(size_of_watermark)
     mainimg = image.copy()
     mainimg.paste(waterimg, (int(tbox1.text()), int(tbox2.text())))
     plt.imshow(mainimg)
     plt.show()


# Black and white
def BW():
    bwimg = image.convert('L')
    plt.imshow(bwimg, cmap='gray')
    plt.show()


# Conerting in different modes of color
colormode = ["RGBA", "HSV", "CMYK"]
combo0 = QComboBox(window)
combo0.setGeometry(1795, 5, 120, 30)
combo0.setStyleSheet(
    'border-radius:17; background-color: rgba(0,0,0,0.7); color: rgba(255,255,255,0.7); border: 1px solid #000000;')
combo0.setFont(QFont('Tw Cen MT (Headings)', 10))
combo0.addItems(colormode)
combo0.show()


def colorm ():
    newforimg = image.convert(str(combo0.currentText()))# HSV, RGBA,
    plt.imshow(newforimg)
    plt.show()


# Image enhancement
def color():
    image0 = image.copy()
    image3 = ImageEnhance.Color(image0).enhance(Sd.value()/100)
    plt.imshow(image3)
    plt.show()


def contrast():
    image0 = image.copy()
    image4 = ImageEnhance.Contrast(image0).enhance(Sd.value()/100)
    plt.imshow(image4)
    plt.show()


def brightness():
    image0 = image.copy()
    image5 = ImageEnhance.Brightness(image0).enhance(Sd.value()/100)
    plt.imshow(image5)
    plt.show()


def sharpness():
    image0 = image.copy()
    image6 = ImageEnhance.Sharpness(image0).enhance(Sd.value()/100)
    plt.imshow(image6)
    plt.show()


# Alpha blending
def alphablend():
     image7 = image.copy()
     filename1 = QFileDialog.getOpenFileName(window, 'Open Image File', "", "Image files (*.jpg *.jpeg *.png)")
     fileimg1 = filename1[0]
     fileimg1 = fileimg1.replace("/", "\\")
     image56 = Image.open(fileimg1)
     image8 = image56.copy()
     image8 = image8.resize(image7.size)
     l0.setText("Set Alpha")
     l0.show()
     Aimage = Image.blend(image7, image8, float(tbox1.text()))
     plt.imshow(Aimage)
     plt.show()


# Flip channels of color
def flipC():
    imgch = image.copy()
    r, g, b = imgch.split()
    im = Image.merge("RGB", (b, g, r))
    plt.imshow(im)
    plt.show()


# Button for Contrast
button0 = Q.QPushButton(window)
button0.setFont(QFont('Tw Cen MT (Headings)', 9))
button0.setText("Contrast")
button0.clicked.connect(contrast)
button0.setGeometry(1825, 140, 90, 30)
button0.setStyleSheet("QPushButton"
                     "{"
                     "background-color : rgba(0, 0, 0, 1);"
                     "border-radius:15;"
                     "color: #ffffff;"
                     "}"
                     "QPushButton::hover"
                     "{""background-color : rgba(165, 241, 246, 0.2);"

                     "}"
                     "QPushButton::pressed"
                     "{""background-color :rgb(122, 214, 255);"
                     "}")


# Button for Brightness
button1 = Q.QPushButton(window)
button1.setFont(QFont('Tw Cen MT (Headings)', 9))
button1.setText("Brightness")
button1.clicked.connect(brightness)
button1.setGeometry(1825, 185, 90, 30)  # 100
button1.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:15;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")


# Button for Color
button2 = Q.QPushButton(window)
button2.setFont(QFont('Tw Cen MT (Headings)', 9))
button2.setText(" Color")
button2.clicked.connect(color)
button2.setGeometry(1825, 230, 90, 30)
button2.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:15;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")


# Button for Sharpness
button3 = Q.QPushButton(window)
button3.setFont(QFont('Tw Cen MT (Headings)', 9))
button3.setText("Sharpness")
button3.clicked.connect(sharpness)
button3.setGeometry(1825, 275, 90, 30)
button3.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:15;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")

# Flip image
# Right to Left flip
button4 = Q.QPushButton(window)
button4.setFont(QFont('Tw Cen MT (Headings)', 9))
button4.setText("RtoL")
button4.clicked.connect(RtoL)
button4.setGeometry(100, 950, 90, 30)
button4.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:15;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")


# Top to bottom flip
button5 = Q.QPushButton(window)
button5.setFont(QFont('Tw Cen MT (Headings)', 9))
button5.setText("TtoB")
button5.clicked.connect(TtoB)
button5.setGeometry(195, 950, 90, 30)
button5.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:15;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")


# BW image
button6 = Q.QPushButton(window)
button6.setFont(QFont('Tw Cen MT (Headings)', 9))
button6.setText("B&W")
button6.clicked.connect(BW)
button6.setGeometry(5, 5, 30, 30)
button6.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:10;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")


# COLOR MODE
button7 = Q.QPushButton(window)
button7.setFont(QFont('Tw Cen MT (Headings)', 9))
button7.setText("Color Mode")
button7.clicked.connect(colorm)
button7.setGeometry(1825, 320, 90, 30)
button7.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:15;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")


# Watermark
button8 = Q.QPushButton(window)
button8.setFont(QFont('Tw Cen MT (Headings)', 9))
button8.setText("WaterMark")
button8.clicked.connect(watermark)
button8.setGeometry(1825, 365, 90, 30)
button8.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:15;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")


# Rotate image
button9 = Q.QPushButton(window)
button9.setFont(QFont('Tw Cen MT (Headings)', 9))
button9.setText("R")
button9.clicked.connect(rotate)
button9.setGeometry(45, 5, 30, 30)
button9.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:10;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")


# Button for AlphaBlend
button01 = Q.QPushButton(window)
button01.setFont(QFont('Tw Cen MT (Headings)', 9))
button01.setText("AlphaBlend")
button01.clicked.connect(alphablend)
button01.setGeometry(1825, 410, 90, 30)
button01.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:15;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")


# Button for CFlip
button02 = Q.QPushButton(window)
button02.setFont(QFont('Tw Cen MT (Headings)', 9))
button02.setText("RGB Flip")
button02.clicked.connect(flipC)
button02.setGeometry(1825, 455, 90, 30)
button02.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:15;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")


# Crop image
button03 = Q.QPushButton(window)
button03.setFont(QFont('Tw Cen MT (Headings)', 9))
button03.setText("C")
button03.clicked.connect(crop)
button03.setGeometry(85, 5, 30, 30)
button03.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:10;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")


# Resize
button04 = Q.QPushButton(window)
button04.setFont(QFont('Tw Cen MT (Headings)', 9))
button04.setText("Resize")
button04.clicked.connect(resize)
button04.setGeometry(5, 950, 90, 30)
button04.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:15;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")


# Button for ImageWaterMark
button05 = Q.QPushButton(window)
button05.setFont(QFont('Tw Cen MT (Headings)', 9))
button05.setText("Imgwater")
button05.clicked.connect(imagewater)
button05.setGeometry(1825, 500, 90, 30)
button05.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:15;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")


# image upload
button06 = Q.QPushButton(window)
button06.setFont(QFont('Tw Cen MT (Headings)', 9))
button06.setText("Upload")
button06.clicked.connect(get_img_file)
button06.setGeometry(290, 950, 90, 30)
button06.setStyleSheet("QPushButton"
                      "{"
                      "background-color : rgba(0, 0, 0, 1);"
                      "border-radius:15;"
                      "color: #ffffff;"
                      "}"
                      "QPushButton::hover"
                      "{""background-color : rgba(165, 241, 246, 0.2);"

                      "}"
                      "QPushButton::pressed"
                      "{""background-color :rgb(122, 214, 255);"
                      "}")



window.showMaximized()
window.show()
app.exec()