# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logincard.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import base64
import binascii
import datetime
import json
import sys
import threading
import time

import pymysql
from Crypto.Cipher import AES
from PyQt5 import QtCore, QtGui, QtWidgets
import xml.dom.minidom as xmldom
import xml.etree.ElementTree as et
import os
import requests
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QMainWindow


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(396, 172)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 20, 161, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 100, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 100, 113, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "金尚美食卡片管理"))
        self.label.setText(_translate("Dialog", "金尚美食卡片管理"))
        self.label_2.setText(_translate("Dialog", "用户名"))
        self.label_3.setText(_translate("Dialog", "密  码"))
        self.pushButton.setText(_translate("Dialog", "登录"))

class Ui_MainWindow(object):
    def __init__(self):
        self.k = 0
        self.pic_pathname = ''
    def setupUi(self, MainWindow):
        self.pic_pathname = ''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 316)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.maintab = QtWidgets.QWidget()
        self.maintab.setObjectName("maintab")
        self.name_labe1 = QtWidgets.QLabel(self.maintab)
        self.name_labe1.setGeometry(QtCore.QRect(80, 80, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.name_labe1.setFont(font)
        self.name_labe1.setObjectName("name_labe1")
        self.btn_find_name = QtWidgets.QPushButton(self.maintab)
        self.btn_find_name.setGeometry(QtCore.QRect(280, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_find_name.setFont(font)
        self.btn_find_name.setObjectName("btn_find_name")
        self.mobile_label = QtWidgets.QLabel(self.maintab)
        self.mobile_label.setGeometry(QtCore.QRect(50, 110, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.mobile_label.setFont(font)
        self.mobile_label.setObjectName("mobile_label")
        self.mobile_show = QtWidgets.QLabel(self.maintab)
        self.mobile_show.setGeometry(QtCore.QRect(130, 110, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.mobile_show.setFont(font)
        self.mobile_show.setObjectName("mobile_show")
        self.precard_label = QtWidgets.QLabel(self.maintab)
        self.precard_label.setGeometry(QtCore.QRect(70, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.precard_label.setFont(font)
        self.precard_label.setObjectName("precard_label")
        self.precard_show = QtWidgets.QLabel(self.maintab)
        self.precard_show.setGeometry(QtCore.QRect(130, 140, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.precard_show.setFont(font)
        self.precard_show.setObjectName("precard_show")
        self.nowcard_label = QtWidgets.QLabel(self.maintab)
        self.nowcard_label.setGeometry(QtCore.QRect(70, 170, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.nowcard_label.setFont(font)
        self.nowcard_label.setObjectName("nowcard_label")
        self.nowcard_show = QtWidgets.QLabel(self.maintab)
        self.nowcard_show.setGeometry(QtCore.QRect(130, 170, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.nowcard_show.setFont(font)
        self.nowcard_show.setObjectName("nowcard_show")
        self.btn_radcard = QtWidgets.QPushButton(self.maintab)
        self.btn_radcard.setGeometry(QtCore.QRect(70, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_radcard.setFont(font)
        self.btn_radcard.setObjectName("btn_radcard")
        self.btn_dealcard = QtWidgets.QPushButton(self.maintab)
        self.btn_dealcard.setGeometry(QtCore.QRect(200, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_dealcard.setFont(font)
        self.btn_dealcard.setObjectName("btn_dealcard")
        self.pic_show = QtWidgets.QLabel(self.maintab)
        self.pic_show.setGeometry(QtCore.QRect(430, 50, 151, 171))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pic_show.setFont(font)
        self.pic_show.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pic_show.setObjectName("pic_show")
        self.pic_label = QtWidgets.QLabel(self.maintab)
        self.pic_label.setGeometry(QtCore.QRect(430, 250, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pic_label.setFont(font)
        self.pic_label.setObjectName("pic_label")
        self.title_label = QtWidgets.QLabel(self.maintab)
        self.title_label.setGeometry(QtCore.QRect(230, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.maintab)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 80, 113, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tabWidget.addTab(self.maintab, "")
        self.maintab2 = QtWidgets.QWidget()
        self.maintab2.setObjectName("maintab2")
        self.btn2_dealcard = QtWidgets.QPushButton(self.maintab2)
        self.btn2_dealcard.setGeometry(QtCore.QRect(200, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn2_dealcard.setFont(font)
        self.btn2_dealcard.setObjectName("btn2_dealcard")
        self.btn_selectpic = QtWidgets.QPushButton(self.maintab2)
        self.btn_selectpic.setGeometry(QtCore.QRect(380, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_selectpic.setFont(font)
        self.btn_selectpic.setObjectName("btn_selectpic")
        self.pic_show2 = QtWidgets.QLabel(self.maintab2)
        self.pic_show2.setGeometry(QtCore.QRect(350, 50, 151, 171))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pic_show2.setFont(font)
        self.pic_show2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pic_show2.setObjectName("pic_show2")
        self.btn2_readcard = QtWidgets.QPushButton(self.maintab2)
        self.btn2_readcard.setGeometry(QtCore.QRect(80, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn2_readcard.setFont(font)
        self.btn2_readcard.setObjectName("btn2_readcard")
        self.btn2_loginuser = QtWidgets.QPushButton(self.maintab2)
        self.btn2_loginuser.setGeometry(QtCore.QRect(80, 220, 212, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn2_loginuser.setFont(font)
        self.btn2_loginuser.setObjectName("btn2_loginuser")
        self.title_label2 = QtWidgets.QLabel(self.maintab2)
        self.title_label2.setGeometry(QtCore.QRect(220, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.title_label2.setFont(font)
        self.title_label2.setObjectName("title_label2")
        self.nowcard_show2 = QtWidgets.QLabel(self.maintab2)
        self.nowcard_show2.setGeometry(QtCore.QRect(160, 150, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nowcard_show2.setFont(font)
        self.nowcard_show2.setObjectName("nowcard_show2")
        self.nowcard_label2 = QtWidgets.QLabel(self.maintab2)
        self.nowcard_label2.setGeometry(QtCore.QRect(100, 150, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nowcard_label2.setFont(font)
        self.nowcard_label2.setObjectName("nowcard_label2")
        self.name_label2 = QtWidgets.QLabel(self.maintab2)
        self.name_label2.setGeometry(QtCore.QRect(110, 50, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.name_label2.setFont(font)
        self.name_label2.setObjectName("name_label2")
        self.mobile_label2 = QtWidgets.QLabel(self.maintab2)
        self.mobile_label2.setGeometry(QtCore.QRect(80, 120, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mobile_label2.setFont(font)
        self.mobile_label2.setObjectName("mobile_label2")
        self.lineEdit = QtWidgets.QLineEdit(self.maintab2)
        self.lineEdit.setGeometry(QtCore.QRect(160, 50, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.tagcombox = QtWidgets.QComboBox(self.maintab2)
        self.tagcombox.setGeometry(QtCore.QRect(160, 85, 121, 20))
        self.taglabel = QtWidgets.QLabel(self.maintab2)
        self.taglabel.setGeometry(QtCore.QRect(80, 85, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.taglabel.setFont(font)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.maintab2)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 120, 121, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tabWidget.addTab(self.maintab2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.maintab3 = QtWidgets.QWidget()
        self.maintab3.setObjectName("maintab3")
        self.tabWidget.addTab(self.maintab3, "")
        self.set_port_name = QtWidgets.QLabel(self.maintab3)
        self.set_port_name.setGeometry(QtCore.QRect(80, 80, 61, 21))
        self.set_port_show = QtWidgets.QComboBox(self.maintab3)
        self.set_port_show.setGeometry(QtCore.QRect(140, 80, 200, 20))
        self.net_addr1 = QtWidgets.QLabel(self.maintab3)
        self.net_addr1.setGeometry(QtCore.QRect(80,110,61,21))
        self.net_addr1_show = QtWidgets.QLineEdit(self.maintab3)
        self.net_addr1_show.setGeometry(QtCore.QRect(140,110,200,20))
        self.net_addr2 = QtWidgets.QLabel(self.maintab3)
        self.net_addr2.setGeometry(QtCore.QRect(80, 140, 61, 21))
        self.net_addr2_show = QtWidgets.QLineEdit(self.maintab3)
        self.net_addr2_show.setGeometry(QtCore.QRect(140, 140, 200, 20))
        self.btn_setting = QtWidgets.QPushButton(self.maintab3)
        self.btn_setting.setGeometry(QtCore.QRect(210, 190, 60, 21))
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name_labe1.setText(_translate("MainWindow", "编号"))
        self.btn_find_name.setText(_translate("MainWindow", "查  找"))
        self.btn_find_name.clicked.connect(self.query_userinfo)
        self.mobile_label.setText(_translate("MainWindow", "姓   名"))
        self.mobile_show.setText(_translate("MainWindow", ""))
        self.precard_label.setText(_translate("MainWindow", "原卡号"))
        self.precard_show.setText(_translate("MainWindow", ""))
        self.nowcard_label.setText(_translate("MainWindow", "现卡号"))
        self.nowcard_show.setText(_translate("MainWindow", ""))
        self.btn_radcard.setText(_translate("MainWindow", "读   卡"))
        self.btn_radcard.clicked.connect(self.read_card)
        self.btn_dealcard.setText(_translate("MainWindow", "制  卡"))
        self.btn_dealcard.clicked.connect(self.deal_card)
        self.pic_show.setText(_translate("MainWindow", ""))
        self.pic_label.setText(_translate("MainWindow", ""))
        self.title_label.setText(_translate("MainWindow", "金尚美食补卡模式"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.maintab), _translate("MainWindow", "补卡模式"))
        self.btn2_dealcard.setText(_translate("MainWindow", "制  卡"))
        self.btn2_loginuser.setText(_translate("MainWindow", "注册新用户"))
        self.btn2_dealcard.clicked.connect(self.deal_card2)
        self.btn_selectpic.setText(_translate("MainWindow", "选择照片"))
        self.btn_selectpic.clicked.connect(self.select_pic)
        self.pic_show2.setText(_translate("MainWindow", ""))
        self.btn2_readcard.setText(_translate("MainWindow", "读   卡"))
        self.btn2_readcard.clicked.connect(self.read_card2)
        self.title_label2.setText(_translate("MainWindow", "金尚美食发卡模式"))
        self.nowcard_show2.setText(_translate("MainWindow", ""))
        self.nowcard_label2.setText(_translate("MainWindow", "现卡号"))
        self.name_label2.setText(_translate("MainWindow", "姓名"))
        self.mobile_label2.setText(_translate("MainWindow", "手机号码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.maintab2), _translate("MainWindow", "发卡模式"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.maintab3), _translate("MainWindow", "设置"))
        self.taglabel.setText(_translate("MainWindow","所属部门"))
        self.set_port_name.setText(_translate("MainWindow","串口号："))
        self.net_addr1.setText(_translate("MainWindow","网址一："))
        self.net_addr2.setText(_translate("MainWindow","网址二："))
        self.btn_setting.setText(_translate("MainWindows","确  定"))
        self.btn_setting.clicked.connect(self.update_setttings)
        self.btn2_loginuser.clicked.connect(self.login_user)
        t2 = threading.Thread(target=self.get_grouptags)
        t2.start()
        self.k = 0
    def query_userinfo(self):
        try:
            xmlfilepath = os.path.abspath("config.xml")
            domobj = xmldom.parse(xmlfilepath)
            elementobj = domobj.documentElement
            subElementObj = elementobj.getElementsByTagName("server")
            addr = subElementObj[0].getAttribute("addr")
            dbElementObj = elementobj.getElementsByTagName("db")
            db_name = dbElementObj[0].getAttribute("name")
            db_user = dbElementObj[0].getAttribute("user")
            db_pwd = dbElementObj[0].getAttribute("pwd")
        except Exception as e:
            log = datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S') + "[配置文件配置错误，错误原因为：" + e.__str__() + "]\n"
            with open('logs.log', 'at', encoding='gbk') as f:
                f.write(log)
            QMessageBox.critical(self,"错误","配置文件错误")
            return
        db = pymysql.connect(addr, db_user, db_pwd, db_name)
        cursor = db.cursor()
        query_sql = "SELECT * FROM charge WHERE phonenum = %s"%self.lineEdit_3.text()
        try:
            cursor.execute(query_sql)
            results = cursor.fetchall()
            print(results)
            if not results:
                log = datetime.datetime.now().strftime(
                    '%Y-%m-%d %H:%M:%S') + "[查找编号为：" + self.lineEdit_3.text() + "的用户，经查找，查无此人]\n"
                with open('logs.log', 'at', encoding='gbk') as f:
                    f.write(log)
                QMessageBox.critical(self, "错误","用户不存在！")
                return
            for rows in results:
                self.mobile_show.setText(rows[1])
                self.precard_show.setText(rows[2])
                # ba = QtCore.QByteArray.fromBase64(rows[5].encode('utf8'))
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(rows[5])
                self.pic_show.setPixmap(pixmap)
                self.pic_show.setScaledContents(True)
        except Exception as e:
            print(e.__str__())
            QMessageBox.critical(self, "错误", e.__str__())
        cursor.close()
        db.close()
    def read_card(self):
        self.k = 0
        self.nowcard_show.setText("请放置IC卡")
        try:
            xmlfilepath = os.path.abspath("config.xml")
            domobj = xmldom.parse(xmlfilepath)
            elementobj = domobj.documentElement
            subElementObj = elementobj.getElementsByTagName("com")
            port_addr = subElementObj[0].getAttribute("name")
            port_rate = subElementObj[0].getAttribute("bitrate")
        except Exception as e:
            log = datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S') + "[配置文件配置错误，错误原因为：" +e.__str__()+ "]\n"
            with open('logs.log', 'at', encoding='gbk') as f:
                f.write(log)
            QMessageBox.critical(self,"错误","配置文件错误")
            return
        try:
            self.x = serial.Serial(port_addr,int(port_rate))
        except Exception as e:
            log = datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S') + "[串口打开失败，失败原因为：" + e.__str__() + "]\n"
            with open('logs.log', 'at', encoding='gbk') as f:
                f.write(log)
            QMessageBox.critical(self, "错误", "串口打开失败！"+e.__str__())
            return
        def read_data():
            while True:
                if self.k == 0:
                    #data =  self.x.readline().decode('utf-8').replace('\n','')
                    data = self.x.read(16)
                    print(data)
                    hex_data = binascii.b2a_hex(data)
                    print(str(hex_data))
                    self.nowcard_show.setText(str(hex_data)[2:-1].upper())
                    self.k == 1
                    self.x.close()
                    break
        t1 = threading.Thread(target=read_data)
        t1.start()
    def deal_card(self):
        post_data = {
            'name':self.lineEdit_3.text(),
            'mobile':self.mobile_show.text(),
            'precard':self.precard_show.text(),
            'nowcard':self.nowcard_show.text()
        }
        try:
            xmlfilepath = os.path.abspath("config.xml")
            domobj = xmldom.parse(xmlfilepath)
            elementobj = domobj.documentElement
            subElementObj = elementobj.getElementsByTagName("server")
            addr = subElementObj[0].getAttribute("addr")
            dbElementObj = elementobj.getElementsByTagName("db")
            db_name = dbElementObj[0].getAttribute("name")
            db_user = dbElementObj[0].getAttribute("user")
            db_pwd = dbElementObj[0].getAttribute("pwd")
        except:
            QMessageBox.critical(self,"错误","配置文件错误")
            return
        db = pymysql.connect(addr, db_user, db_pwd, db_name)
        cursor = db.cursor()
        query_sql = "SELECT * FROM charge WHERE icnum = '%s'"%self.nowcard_show.text()
        update_sql = "UPDATE charge SET icnum= %s WHERE phonenum = %s"
        try:
            cursor.execute(query_sql)
            results = cursor.fetchone()
            if not results:
                cursor.close()
                cursor = db.cursor()
                cursor.execute(update_sql,(self.nowcard_show.text(),self.lineEdit_3.text()))
                db.commit()
                QMessageBox.information(self,"成功","补卡成功！")
                log = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"["+self.lineEdit_3.text()+self.mobile_show.text()+"成功补卡,原卡号:"+self.precard_show.text()+"，现卡号："+self.nowcard_show.text()+"]\n"
                with open('logs.log', 'at', encoding='gbk') as f:
                    f.write(log)
                self.lineEdit_3.clear()
                self.mobile_show.clear()
                self.precard_show.clear()
                self.nowcard_show.clear()
                self.pic_show.clear()
            else:
                log = datetime.datetime.now().strftime(
                    '%Y-%m-%d %H:%M:%S') + "[" + self.lineEdit_3.text() + self.mobile_show.text() + "补卡失败,原卡号:" + self.precard_show.text() + "，预补卡号为：" + self.nowcard_show.text() + "失败原因为：该卡已被使用，使用人为：" + results[1] + "]\n"
                with open('logs.log', 'at', encoding='gbk') as f:
                    f.write(log)
                QMessageBox.information(self, "失败", "该卡已被使用！使用人为：" + results[1])
        except Exception as e:
            db.rollback()
            log = datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S') + "[" + self.lineEdit_3.text() + self.mobile_show.text() + "补卡失败,原卡号:" + self.precard_show.text() + "，预补卡号为：" + self.nowcard_show.text() + "失败原因为："+e.__str__()+"]\n"
            with open('logs.log', 'at', encoding='gbk') as f:
                f.write(log)
            QMessageBox.information(self, "失败", "制卡失败，错误为："+e.__str__())

    def select_pic(self):
        self.pic_pathname, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(self.pic_pathname).scaled(self.pic_show2.width(), self.pic_show2.height())
        self.pic_show2.setPixmap(jpg)
    def read_card2(self):
        self.j = 0
        self.nowcard_show2.setText("请放置IC卡")
        try:
            xmlfilepath = os.path.abspath("config.xml")
            domobj = xmldom.parse(xmlfilepath)
            elementobj = domobj.documentElement
            subElementObj = elementobj.getElementsByTagName("com")
            port_addr = subElementObj[0].getAttribute("name")
            port_rate = subElementObj[0].getAttribute("bitrate")
        except:
            QMessageBox.critical(self, "错误", "配置文件错误")
            return
        self.x = serial.Serial(port_addr, int(port_rate))
        def read_data():
            while True:
                if self.j == 0:
                    data = self.x.read(16)
                    print(data)
                    hex_data = binascii.b2a_hex(data)
                    self.nowcard_show2.setText(str(hex_data)[2:-1])
                    self.k == 1
                    self.x.close()
                    break

        t1 = threading.Thread(target=read_data)
        t1.start()
    def deal_card2(self):
        s = ''
        name = self.lineEdit.text()
        mobile = self.lineEdit_2.text()
        card_num = self.nowcard_show2.text()
        if name == '':
            QMessageBox.critical(self, "错误", "用户名不能为空！")
            return None
        elif mobile == '':
            QMessageBox.critical(self, "错误", "手机号不能为空！")
            return None
        elif card_num == '':
            QMessageBox.critical(self, "错误", "卡号不能为空！")
            return None
        if self.pic_pathname == '':
            QMessageBox.critical(self, "错误", "请选择照片！")
        else:
            try:
                xmlfilepath = os.path.abspath("config.xml")
                domobj = xmldom.parse(xmlfilepath)
                elementobj = domobj.documentElement
                subElementObj = elementobj.getElementsByTagName("server")
                addr = subElementObj[0].getAttribute("addr")
                addr2 = subElementObj[0].getAttribute("addr2")
            except:
                QMessageBox.critical(self,"错误","配置文件错误")
                return
            post_data = {
                "time":time.strftime("%Y-%m-%d %H:%M:%S"),
                "mobile":self.lineEdit_2.text()
            }
            post_data_encrypto = json.dumps(post_data)
            bs = 16
            PADDING = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
            model = AES.MODE_ECB
            str1 = time.strftime("%Y%m%d")
            str2 = str1 + str1[::-1]
            obj = AES.new(str2, model)
            enctypto_text = obj.encrypt(PADDING(post_data_encrypto.replace("'", "\"")).encode('utf-8'))
            enctypto_final = base64.b64encode(enctypto_text)
            post_data_send = {
                "contents": str(enctypto_final)[2:-1]
            }
            print(addr)
            try:
                r = requests.post(addr2 + "api/user/show", post_data_send)
                print(r.text)
                r_json = json.loads(r.text)
                if r_json.get('code') == 0:
                    with open(self.pic_pathname, 'rb') as f:
                        base64_data = base64.b64encode(f.read())
                        s = base64_data.decode()
                    post_data = {
                        'name':name,
                        'mobile':mobile,
                        'nowcard':card_num,
                        'pic_num':s
                    }
                    r2 = requests.post(addr+"app01/adduser/",post_data)

                    print(r2.text)
                    return_data = json.loads(r2.text)

                    if return_data.get('code') == '0':
                        QMessageBox.information(self, "成功", "数据已提交，业务客户端重启后生效！")
                        return
                    elif return_data.get('code') == '7':
                        QMessageBox.critical(self, "错误", "该IC卡已被使用！")
                        return
                else:
                    QMessageBox.critical(self, "错误", "此用户在线上不存在")
                    return
            except:
                QMessageBox.critical(self, "错误", "制卡失败")
                return
    def get_grouptags(self):
        self.statusbar.showMessage("正在获取分组信息。。。。。。")
        port_list = list(serial.tools.list_ports.comports())
        for item in port_list:
            self.set_port_show.addItem(item.__str__())
            print(item.device)
        try:
            xmlfilepath = os.path.abspath("config.xml")
            domobj = xmldom.parse(xmlfilepath)
            elementobj = domobj.documentElement
            subElementObj = elementobj.getElementsByTagName("server")
            server_addr = subElementObj[0].getAttribute("addr2")
            local_addr = subElementObj[0].getAttribute("addr")
            self.net_addr2_show.setText(server_addr)
            self.net_addr1_show.setText(local_addr)
        except:
            QMessageBox.critical(self,"错误","配置文件错误")
            return
        bs = 16
        PADDING = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
        model = AES.MODE_ECB
        str1 = time.strftime("%Y%m%d")
        str2 = str1+str1[::-1]
        post_data = {
            "time":time.strftime("%Y-%m-%d %H:%M:%S")
        }
        obj = AES.new(str2,model)
        enctypto_text = obj.encrypt(PADDING(str(post_data).replace("'","\"")).encode('utf-8'))
        enctypto_final = base64.b64encode(enctypto_text)
        post_data_send = {
            "contents":str(enctypto_final)[2:-1]
        }
        try:
            r = requests.post(server_addr+"api/tags/group",post_data_send)
            print(r.text)
            r_json = json.loads(r.text)
            if r_json.get('code') == 0:
                r_json_data = r_json.get('data')
                print(r_json_data)
                self.tagcombox.addItem("请选择部门")
                dict = []
                for key,value in r_json_data.items():
                    dict.append(str(int(key)-1)+'-'+value)
                dict.reverse()
                self.tagcombox.addItems(dict)
                self.statusbar.showMessage("分组信息获取成功")
        except Exception:
            QMessageBox.critical(self, "错误", "无法获取用户分组,请检查网络后重启程序！")
            return
    def login_user(self):
        name_label = self.lineEdit.text()
        mobile_label = self.lineEdit_2.text()
        if name_label == '':
            QMessageBox.critical(self, "错误", "用户名不能为空！")
            return
        if mobile_label == '':
            QMessageBox.critical(self, "错误", "手机号不能为空！")
            return
        if self.tagcombox.currentText() == "请选择部门":
            QMessageBox.critical(self, "错误", "请选择部门！")
            return
        tag_index = self.tagcombox.currentText().split('-')
        try:
            xmlfilepath = os.path.abspath("config.xml")
            domobj = xmldom.parse(xmlfilepath)
            elementobj = domobj.documentElement
            subElementObj = elementobj.getElementsByTagName("server")
            server_addr = subElementObj[0].getAttribute("addr2")
        except:
            QMessageBox.critical(self,"错误","配置文件错误")
            return
        post_data = {
            "name": name_label,
            "mobile": mobile_label,
            "tag": str(int(tag_index[0]) + 1)
        }
        post_data_encrypto = json.dumps(post_data)
        bs = 16
        PADDING = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
        model = AES.MODE_ECB
        str1 = time.strftime("%Y%m%d")
        str2 = str1+str1[::-1]
        obj = AES.new(str2,model)
        enctypto_text = obj.encrypt(PADDING(post_data_encrypto.replace("'","\"")).encode('utf-8'))
        enctypto_final = base64.b64encode(enctypto_text)
        post_data_send = {
            "contents":str(enctypto_final)[2:-1]
        }
        r = requests.post(server_addr+"api/user/register",post_data_send)
        r_json = json.loads(r.text)
        if r_json.get('code') == 0:
            QMessageBox.information(self, "成功", "用户"+name_label+"注册成功！")
            self.lineEdit.setReadOnly(True)
            self.lineEdit_2.setReadOnly(True)
    def update_setttings(self):
        try:
            tree = et.parse('config.xml')
            root = tree.getroot()
            for server in root.iter('server'):
                server.set('addr',self.net_addr1_show.text())
                server.set('addr2',self.net_addr2_show.text())
            com_port = self.set_port_show.currentText().split('-')[0]
            for ports in root.iter('com'):
                ports.set('name',com_port.strip())
            tree.write('config.xml')
            QMessageBox.information(self, "成功", "修改配置文件成功！")
        except:
            QMessageBox.critical(self,"错误","配置文件错误")
            return
class main_frame(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(main_frame, self).__init__()
        self.setupUi(self)
class login_frame(QMainWindow,Ui_Dialog):
    def __init__(self):
        super(login_frame,self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = login_frame()
    widget2 = main_frame()
    def deal_login(self):
        user = widget.lineEdit.text()
        pwd = widget.lineEdit_2.text()
        print(user, pwd)
        if user == '100100' and pwd == '776677':
            widget.lineEdit.clear()
            widget.lineEdit_2.clear()
            widget.hide()
            widget2.show()
    widget.pushButton.clicked.connect(deal_login)
    widget.show()
    sys.exit(app.exec())

