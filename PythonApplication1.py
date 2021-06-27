#!python3.9
# -*- coding: utf-8 -*-

import sys
#загрузка библиотеки sqlite3
import sqlite3
import io
#импорт классов
from PyQt5 import QtCore, QtGui, QtWidgets
#импорт виджетов
from PyQt5.QtWidgets import*
#импорт элементов menubar 
from PyQt5.QtGui import*
#импорт uic файла
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.con = sqlite3.connect("1.db")
        #self.pushButton.clicked.connect(self.initUI)
        #self.pushButton_2.clicked.connect(self.initUI)
        #self.pushButton_3.clicked.connect(self.initUI)
        #self.pushButton_4.clicked.connect(self.initUI)
        #self.pushButton_5.clicked.connect(self.initUI)
        #self.pushButton_6.clicked.connect(self.initUI)
        #self.pushButton_7.clicked.connect(self.initUI)
        self.pushButton_Add.clicked.connect(self.save_results)
        self.pushButton_Search.clicked.connect(self.search_notes)
        self.init_handlers()
        self.modified = {}

    #Проблема в этом ######################################################
    def save_results(self):
        cur = self.con.cursor()
        que = "UPDATE notes SET\n"
        for key in self.modified.keys():
            que += "{}='{}'\n".format(key, self.modified.get(key))
        que += "WHERE id = ?"
        cur.execute(que)
        self.con.commit()
        self.con.commit()
        self.modified = {}

    def search_notes(self):
        cursor = self.con.cursor()
        try:
            # поставил незавизимость от регистра
            request = f"SELECT * from notes WHERE {self.comboBox.currentText()}='" \
                      f"{self.lineEdit.text().lower().capitalize()}'"
            result = cursor.execute(request).fetchall()
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(2)
            self.titles = [description[0] for description in cursor.description][:-2]
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    if isinstance(val, bytes):
                        """ Если полученное значение - поток байтов, это картинка
                            Пребразовываем байты в картинку, изменяем её размер
                        """
                        bytes_io = io.BytesIO(val)
                    else:
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            if len(result[0][-1]) > 0:
                self.plainTextEdit.setPlainText(result[0][-1])
            else:
                self.plainTextEdit.setPlainText('Описание отсутствует')
        except Exception as e:
            # Отлавливаю возникающие ошибки, сообщаю о них пользователю
            print(e.__str__())
            QMessageBox.critical(self, "Ошибка ", "Неверные данные", QMessageBox.Ok)
        cursor.close()

    # обработка нажатия для октрытия 2го окна
    def init_handlers(self):  
        self.pushButton_NewForm.clicked.connect(self.show_MainWindow2)
        self.pushButton_NewForm.clicked.connect(self.Name)

    # открытие 2го окна 
    def show_MainWindow2(self):
        self.window = MainWindow2()
        self.modified = {}

    def Name(self):
        a = self.lineEdit.text()

    def openDialog(self):
        dialog = ClassDialog(self)
        dialog.exec_()
    
    def initUI(self):
        pass

#################################################################################################
class MainWindow2(QMainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()
        
        self.resize(700, 500)
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
       
       ##############################################
       #  Строим меню файла                         #
       ##############################################

        #меню файла - пункт Exit
        exitAction = QAction(QIcon('exit.png'), '&Выйти', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Закрыть заметки')
        exitAction.triggered.connect(qApp.quit)
 
        #меню файла - пункт New
        newAction = QAction(QIcon('new.png'), '&Новая', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Новая заметка')
        newAction.triggered.connect(self.newFile)
        
        #меню файла - пункт Open
        openAction = QAction(QIcon('open.png'), '&Открыть', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Открыть файл')
        openAction.triggered.connect(self.openFile)
        
        #меню файла - пункт Save As
        saveasAction = QAction(QIcon('save_as.png'), '&Сохранить как', self)
        saveasAction.setShortcut('Ctrl+S')
        saveasAction.setStatusTip('Сохранить файл как...')
        saveasAction.triggered.connect(self.saveAs)
        self.statusBar()
 
        #добавляем элементы в меню
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Меню')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveasAction)
        fileMenu.addAction(exitAction)
        self.setWindowIcon(QIcon('1.png'))
        self.setGeometry(600, 300, 300, 200)
        self.setWindowTitle('Новая заметка')
        self.show()
        
    def newFile(self):
        self.textEdit.setText("")
    
    def openFile(self):
        #диалог открытия файла 
        fname = QFileDialog.getOpenFileName(self, 'Открыть файл')[0]
        openedFile = open(fname, 'r')
        txt = openedFile.read()
        openedFile.close()
        self.textEdit.setText(txt)
    
    def saveAs(self):
        #диалог сохранения файла 
        fname = QFileDialog.getSaveFileName(self)[0]
        openedFile = open(fname, 'w')
        txt = self.textEdit.toPlainText()
        openedFile.write(txt)
        openedFile.close()

###############################################################################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
