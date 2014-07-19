#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
The Kittens project

author: Rishabh Bhargava

"""

import sys
from PyQt4 import QtGui
from urllib2 import urlopen
import requests

class Kitten(QtGui.QWidget):

	def __init__(self):
		super(Kitten, self).__init__()

		self.initUI()

	def initUI(self):

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle("KittenApp")
		self.setWindowIcon(QtGui.QIcon('kitten_icon.png'))

		self.height_label = QtGui.QLabel("Enter height: ", self)
		self.height_label.move(10,10)

		self.width_label = QtGui.QLabel("Enter width: ", self)
		self.width_label.move(10, 40)

		self.file_name_label = QtGui.QLabel("What name? ", self)
		self.file_name_label.move(10, 70)

		self.ok_button = QtGui.QPushButton('Click me', self)
		self.ok_button.resize(self.ok_button.sizeHint())
		self.ok_button.move(150,120)
		self.ok_button.setToolTip("Please <b>Click</b> me!")
		self.ok_button.clicked.connect(self.ok_button_clicked)

		self.height_line_edit = QtGui.QLineEdit(self)
		self.height_line_edit.move(100, 10)

		self.width_line_edit = QtGui.QLineEdit(self)
		self.width_line_edit.move(100, 40)

		self.file_name_line_edit = QtGui.QLineEdit(self)
		self.file_name_line_edit.move(100, 70)

		self.show()

	def ok_button_clicked(self):
		
		if is_number(str(self.height_line_edit.text())) and is_number(str(self.width_line_edit.text())):
			
			save_image(str(self.height_line_edit.text()), str(self.width_line_edit.text()), str(self.file_name_line_edit.text()))
			self.height_line_edit.clear()
			self.width_line_edit.clear()
			self.file_name_line_edit.clear()

		else:
			error = QtGui.QMessageBox()
			error.setText("Check the height and width fields again!")
			error.exec_()

def save_image(height, width, name):
	url = "http://placekitten.com/" + width + "/" + height


	kittens = urlopen(url)
	response = kittens.read()

	file_name = name + ".jpeg"

	file_kitten = open(file_name, "w")
	file_kitten.write(response)
	file_kitten.close()

def main():

	app = QtGui.QApplication(sys.argv)
	kit = Kitten()
	sys.exit(app.exec_())

def is_number(num):
	 try:
	 	float(num)
	 except:
	 	return False
	 return True

if __name__ == '__main__':
	main()

