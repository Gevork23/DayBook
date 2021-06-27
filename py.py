# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 540)
        MainWindow.setMinimumSize(QtCore.QSize(860, 540))
        MainWindow.setMaximumSize(QtCore.QSize(860, 540))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-image:  url(👍🏻.png);")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(149, 0, 711, 399))
        self.textBrowser.setStyleSheet("background-image: url(Фон.jpg);")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_Settings = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Settings.setEnabled(True)
        self.pushButton_Settings.setGeometry(QtCore.QRect(40, 310, 35, 35))
        self.pushButton_Settings.setMaximumSize(QtCore.QSize(36, 36))
        self.pushButton_Settings.setTabletTracking(False)
        self.pushButton_Settings.setDefault(False)
        self.pushButton_Settings.setFlat(False)
        self.pushButton_Settings.setObjectName("pushButton_Settings")
        self.pushButton_Notifications = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Notifications.setGeometry(QtCore.QRect(0, 310, 35, 35))
        self.pushButton_Notifications.setMaximumSize(QtCore.QSize(36, 36))
        self.pushButton_Notifications.setTabletTracking(False)
        self.pushButton_Notifications.setText("")
        self.pushButton_Notifications.setObjectName("pushButton_Notifications")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 24, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 48, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 72, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 96, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 120, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 144, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_NewForm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_NewForm.setGeometry(QtCore.QRect(800, 430, 30, 30))
        self.pushButton_NewForm.setStyleSheet("background-image: url(1.png);")
        self.pushButton_NewForm.setText("")
        self.pushButton_NewForm.setObjectName("pushButton_NewForm")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 410, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(610, 430, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DayBook"))
        self.pushButton.setText(_translate("MainWindow", "Заметки"))
        self.pushButton_2.setText(_translate("MainWindow", "Мой день"))
        self.pushButton_3.setText(_translate("MainWindow", "Важные"))
        self.pushButton_4.setText(_translate("MainWindow", "Запланированные"))
        self.pushButton_5.setText(_translate("MainWindow", "Задачи"))
        self.pushButton_6.setText(_translate("MainWindow", "Сегодня"))
        self.pushButton_7.setText(_translate("MainWindow", "Новая категория"))
        self.label.setText(_translate("MainWindow", "Заголовок"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())