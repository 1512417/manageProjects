print("\n> Management Tool\n")
print("> Connecting to data...\n")
import sys
import subprocess
import sqlite3

from datetime import date
from functools import partial
from PySide2 import QtCore, QtGui, QtWidgets

font = QtGui.QFont()
font.setFamily("Comic Sans MS")
font.setPointSize(13)
font.setWeight(70)

def CreateDb():
	con = sqlite3.connect(r'.\Management.db')	
	cur = con.cursor()	
	cur.executescript("""DROP TABLE IF EXISTS Management;
					CREATE TABLE Management(Project CHAR, Tool Name CHAR, Start Day CHAR, Software CHAR, Progress CHAR, Deadline INT, Notes NVARCHAR);""")
	con.close()
class Ui_MainWindow(object):
	def Ui(self, MainWindow):
		MainWindow.setObjectName("MainWindow")	
		MainWindow.resize(780,700)
		MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Management Tool", None, -1))

		today = date.today()
		today = today.strftime("%d/%m/%Y")
		self.label_1 = QtWidgets.QLabel(MainWindow)
		self.label_1.setGeometry(QtCore.QRect(10, 10, 590, 31))
		self.label_1.setFont(font)
		self.label_1.setObjectName("label")
		self.label_1.setText(QtWidgets.QApplication.translate("MainWindow", "Date: {}".format(str(today)), None, -1))

		self.tableWidget = QtWidgets.QTableWidget(MainWindow)
		self.tableWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
		self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
		self.tableWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
		self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
		self.tableWidget.setGeometry(QtCore.QRect(10, 40, 750, 600))
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(7)
		self.tableWidget.setRowCount(100)

		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(6, item)
		
		self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "Project", None, -1))
		self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "Tool Name", None, -1))
		self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "Software", None, -1))
		self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "Progress", None, -1))
		self.tableWidget.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("MainWindow", "Start Day", None, -1))
		self.tableWidget.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("MainWindow", "Deadline", None, -1))
		self.tableWidget.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("MainWindow", "Notes", None, -1))
		self.tableWidget.horizontalHeader().setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

		self.pushButton = QtWidgets.QPushButton(MainWindow)
		self.pushButton.setGeometry(QtCore.QRect(500, 650, 220, 41))
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Save to Database", None, -1))
		self.pushButton.clicked.connect(partial(self.save))

		self.pushButton_1 = QtWidgets.QPushButton(MainWindow)
		self.pushButton_1.setGeometry(QtCore.QRect(250, 650, 220, 41))
		self.pushButton_1.setFont(font)
		self.pushButton_1.setObjectName("pushButton_1")
		self.pushButton_1.setText(QtWidgets.QApplication.translate("MainWindow", "Reset Database", None, -1))
		self.pushButton_1.clicked.connect(partial(self.resetDatabase))

		self.showData()
		MainWindow.show()

	def resetDatabase(self):
		CreateDb()
		msg = QtWidgets.QMessageBox()
		msg.setIcon(msg.Information)
		msg.setText("Reset Data Successfully!")
		msg.setWindowTitle("Announcement")
		msg.exec_()

	def save(self):
		CreateDb()
		con = sqlite3.connect(r'.\Management.db')
		row = 0
		while row < 20:
			data = []			
			for i in range (0,7):
				item = self.tableWidget.item(row, i)
				print(item)
				try:
					data.append(item.text())
				except:
					data.append("")
			data = tuple(data)
			cur = con.cursor()
			cur.execute('INSERT INTO Management VALUES(?, ?, ?, ?, ?, ?, ?)', data)
			row += 1
			con.commit()

		con.close()
		msg = QtWidgets.QMessageBox()
		msg.setIcon(msg.Information)
		msg.setText("Saving Data Successfully!")
		msg.setWindowTitle("Announcement")
		msg.exec_()

	def showData(self):
		con = sqlite3.connect(r'.\Management.db')
		cur = con.cursor()
		result = cur.execute("SELECT * FROM Management")
		for row_number, row_data in enumerate(result):
			for column_number, data in enumerate(row_data):
				self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
		con.close()

app = QtWidgets.QApplication(sys.argv)
ui = Ui_MainWindow()
dialog = QtWidgets.QWidget()
ui.Ui(dialog)
dialog.activateWindow()
sys.exit(app.exec_())

con = sqlite3.connect(r'C:\Users\phuong.phung\Desktop\ManagementTool\Management.db')		
cur = con.cursor()	
cur.execute('SELECT * FROM Management')
data = cur.fetchall()
print(data)
con.close()