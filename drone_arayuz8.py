

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from __future__ import print_function #...
import sys #......
import time 
import math
import cv2
import imutils
import numpy as np
from pymavlink import mavutil

durumstr= "durum mesaj çubugu"
R = 6378.137

yaw1 = 0
from PyQt5 import QtCore, QtGui, QtWidgets

from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal

vehicle = connect("udp:127.0.0.1:14551", wait_ready=True)
class Ui_MainWindow(object):
    durumstr= "durum mesaj çubugu"
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 310, 162, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.iki = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.iki.setContentsMargins(0, 0, 0, 0)
        self.iki.setObjectName("iki")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.arm_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.arm_yazi_alani.setObjectName("arm_yazi_alani")
        self.horizontalLayout_7.addWidget(self.arm_yazi_alani)
        self.armed_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.armed_buton.setObjectName("armed_buton")
        self.horizontalLayout_7.addWidget(self.armed_buton)
        self.iki.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.x_hizi_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.x_hizi_yazi_alani.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.x_hizi_yazi_alani.setObjectName("x_hizi_yazi_alani")
        self.horizontalLayout_8.addWidget(self.x_hizi_yazi_alani)
        self.x_hizi_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.x_hizi_buton.setObjectName("x_hizi_buton")
        self.horizontalLayout_8.addWidget(self.x_hizi_buton)
        self.iki.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.y_hizi_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.y_hizi_yazi_alani.setObjectName("y_hizi_yazi_alani")
        self.horizontalLayout_9.addWidget(self.y_hizi_yazi_alani)
        self.y_hizi_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.y_hizi_buton.setObjectName("y_hizi_buton")
        self.horizontalLayout_9.addWidget(self.y_hizi_buton)
        self.iki.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.z_hizi_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.z_hizi_yazi_alani.setObjectName("z_hizi_yazi_alani")
        self.horizontalLayout_10.addWidget(self.z_hizi_yazi_alani)
        self.z_hizi_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.z_hizi_buton.setObjectName("z_hizi_buton")
        self.horizontalLayout_10.addWidget(self.z_hizi_buton)
        self.iki.addLayout(self.horizontalLayout_10)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(180, 310, 171, 201))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.uc = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.uc.setContentsMargins(0, 0, 0, 0)
        self.uc.setObjectName("uc")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.yaw_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.yaw_yazi_alani.setObjectName("yaw_yazi_alani")
        self.horizontalLayout_13.addWidget(self.yaw_yazi_alani)
        self.yaw_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.yaw_buton.setObjectName("yaw_buton")
        self.horizontalLayout_13.addWidget(self.yaw_buton)
        self.uc.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pitch_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.pitch_yazi_alani.setObjectName("pitch_yazi_alani")
        self.horizontalLayout_11.addWidget(self.pitch_yazi_alani)
        self.pitch_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pitch_buton.setObjectName("pitch_buton")
        self.horizontalLayout_11.addWidget(self.pitch_buton)
        self.uc.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.roll_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.roll_yazi_alani.setObjectName("roll_yazi_alani")
        self.horizontalLayout_12.addWidget(self.roll_yazi_alani)
        self.roll_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.roll_buton.setObjectName("roll_buton")
        self.horizontalLayout_12.addWidget(self.roll_buton)
        self.uc.addLayout(self.horizontalLayout_12)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(360, 310, 291, 211))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.dort = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.dort.setContentsMargins(0, 0, 0, 0)
        self.dort.setObjectName("dort")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.wp1_enlem_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp1_enlem_yazi_alani.setObjectName("wp1_enlem_yazi_alani")
        self.horizontalLayout_16.addWidget(self.wp1_enlem_yazi_alani)
        self.wp1_boylam_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp1_boylam_yazi_alani.setObjectName("wp1_boylam_yazi_alani")
        self.horizontalLayout_16.addWidget(self.wp1_boylam_yazi_alani)
        self.wp1_yukseklik_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp1_yukseklik_yazi_alani.setObjectName("wp1_yukseklik_yazi_alani")
        self.horizontalLayout_16.addWidget(self.wp1_yukseklik_yazi_alani)
        self.wp1_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.wp1_buton.setObjectName("wp1_buton")
        self.horizontalLayout_16.addWidget(self.wp1_buton)
        self.dort.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.wp2_enlem_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp2_enlem_yazi_alani.setObjectName("wp2_enlem_yazi_alani")
        self.horizontalLayout_15.addWidget(self.wp2_enlem_yazi_alani)
        self.wp2_boylam_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp2_boylam_yazi_alani.setObjectName("wp2_boylam_yazi_alani")
        self.horizontalLayout_15.addWidget(self.wp2_boylam_yazi_alani)
        self.wp2_yukseklik_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp2_yukseklik_yazi_alani.setObjectName("wp2_yukseklik_yazi_alani")
        self.horizontalLayout_15.addWidget(self.wp2_yukseklik_yazi_alani)
        self.wp2_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.wp2_buton.setObjectName("wp2_buton")
        self.horizontalLayout_15.addWidget(self.wp2_buton)
        self.dort.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.wp3_enlem_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp3_enlem_yazi_alani.setObjectName("wp3_enlem_yazi_alani")
        self.horizontalLayout_14.addWidget(self.wp3_enlem_yazi_alani)
        self.wp3_boylam_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp3_boylam_yazi_alani.setObjectName("wp3_boylam_yazi_alani")
        self.horizontalLayout_14.addWidget(self.wp3_boylam_yazi_alani)
        self.wp3_yukseklik_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp3_yukseklik_yazi_alani.setObjectName("wp3_yukseklik_yazi_alani")
        self.horizontalLayout_14.addWidget(self.wp3_yukseklik_yazi_alani)
        self.wp3_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.wp3_buton.setObjectName("wp3_buton")
        self.horizontalLayout_14.addWidget(self.wp3_buton)
        self.dort.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.wp4_enlem_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp4_enlem_yazi_alani.setObjectName("wp4_enlem_yazi_alani")
        self.horizontalLayout_18.addWidget(self.wp4_enlem_yazi_alani)
        self.wp4_boylam_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp4_boylam_yazi_alani.setObjectName("wp4_boylam_yazi_alani")
        self.horizontalLayout_18.addWidget(self.wp4_boylam_yazi_alani)
        self.wp4_yukseklik_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp4_yukseklik_yazi_alani.setObjectName("wp4_yukseklik_yazi_alani")
        self.horizontalLayout_18.addWidget(self.wp4_yukseklik_yazi_alani)
        self.wp4_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.wp4_buton.setObjectName("wp4_buton")
        self.horizontalLayout_18.addWidget(self.wp4_buton)
        self.dort.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.wp5_enlem_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp5_enlem_yazi_alani.setObjectName("wp5_enlem_yazi_alani")
        self.horizontalLayout_17.addWidget(self.wp5_enlem_yazi_alani)
        self.wp5_boylam_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp5_boylam_yazi_alani.setObjectName("wp5_boylam_yazi_alani")
        self.horizontalLayout_17.addWidget(self.wp5_boylam_yazi_alani)
        self.wp5_yukseklik_yazi_alani = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.wp5_yukseklik_yazi_alani.setObjectName("wp5_yukseklik_yazi_alani")
        self.horizontalLayout_17.addWidget(self.wp5_yukseklik_yazi_alani)
        self.wp5_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.wp5_buton.setObjectName("wp5_buton")
        self.horizontalLayout_17.addWidget(self.wp5_buton)
        self.dort.addLayout(self.horizontalLayout_17)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 287, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.bir = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.bir.setContentsMargins(0, 0, 0, 0)
        self.bir.setObjectName("bir")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boylam = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.boylam.setFrameShape(QtWidgets.QFrame.Box)
        self.boylam.setObjectName("boylam")
        self.horizontalLayout.addWidget(self.boylam)
        self.enlem = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.enlem.setFrameShape(QtWidgets.QFrame.Box)
        self.enlem.setObjectName("enlem")
        self.horizontalLayout.addWidget(self.enlem)
        self.yukseklik = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.yukseklik.setFrameShape(QtWidgets.QFrame.Box)
        self.yukseklik.setObjectName("yukseklik")
        self.horizontalLayout.addWidget(self.yukseklik)
        self.bir.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.enlem_bilgisi = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.enlem_bilgisi.setFrameShape(QtWidgets.QFrame.Box)
        self.enlem_bilgisi.setText("")
        self.enlem_bilgisi.setObjectName("enlem_bilgisi")
        self.horizontalLayout_2.addWidget(self.enlem_bilgisi)
        self.boylam_bilgisi = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.boylam_bilgisi.setFrameShape(QtWidgets.QFrame.Box)
        self.boylam_bilgisi.setText("")
        self.boylam_bilgisi.setObjectName("boylam_bilgisi")
        self.horizontalLayout_2.addWidget(self.boylam_bilgisi)
        self.yukseklik_bilgisi = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.yukseklik_bilgisi.setFrameShape(QtWidgets.QFrame.Box)
        self.yukseklik_bilgisi.setText("")
        self.yukseklik_bilgisi.setObjectName("yukseklik_bilgisi")
        self.horizontalLayout_2.addWidget(self.yukseklik_bilgisi)
        self.bir.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mod = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mod.setFrameShape(QtWidgets.QFrame.Box)
        self.mod.setObjectName("mod")
        self.horizontalLayout_3.addWidget(self.mod)
        self.batarya = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.batarya.setFrameShape(QtWidgets.QFrame.Box)
        self.batarya.setObjectName("batarya")
        self.horizontalLayout_3.addWidget(self.batarya)
        self.hiz = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hiz.setFrameShape(QtWidgets.QFrame.Box)
        self.hiz.setObjectName("hiz")
        self.horizontalLayout_3.addWidget(self.hiz)
        self.bir.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mod_bilgisi = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mod_bilgisi.setFrameShape(QtWidgets.QFrame.Box)
        self.mod_bilgisi.setText("")
        self.mod_bilgisi.setObjectName("mod_bilgisi")
        self.horizontalLayout_4.addWidget(self.mod_bilgisi)
        self.batarya_bilgisi = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.batarya_bilgisi.setFrameShape(QtWidgets.QFrame.Box)
        self.batarya_bilgisi.setText("")
        self.batarya_bilgisi.setObjectName("batarya_bilgisi")
        self.horizontalLayout_4.addWidget(self.batarya_bilgisi)
        self.hiz_bilgisi = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hiz_bilgisi.setFrameShape(QtWidgets.QFrame.Box)
        self.hiz_bilgisi.setText("")
        self.hiz_bilgisi.setObjectName("hiz_bilgisi")
        self.horizontalLayout_4.addWidget(self.hiz_bilgisi)
        self.bir.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.yaw = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.yaw.setFrameShape(QtWidgets.QFrame.Box)
        self.yaw.setObjectName("yaw")
        self.horizontalLayout_5.addWidget(self.yaw)
        self.pitch = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.pitch.setFrameShape(QtWidgets.QFrame.Box)
        self.pitch.setObjectName("pitch")
        self.horizontalLayout_5.addWidget(self.pitch)
        self.roll = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.roll.setFrameShape(QtWidgets.QFrame.Box)
        self.roll.setObjectName("roll")
        self.horizontalLayout_5.addWidget(self.roll)
        self.bir.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.yaw_bilgisi = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.yaw_bilgisi.setFrameShape(QtWidgets.QFrame.Box)
        self.yaw_bilgisi.setText("")
        self.yaw_bilgisi.setObjectName("yaw_bilgisi")
        self.horizontalLayout_6.addWidget(self.yaw_bilgisi)
        self.pitch_bilgisi = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.pitch_bilgisi.setFrameShape(QtWidgets.QFrame.Box)
        self.pitch_bilgisi.setText("")
        self.pitch_bilgisi.setObjectName("pitch_bilgisi")
        self.horizontalLayout_6.addWidget(self.pitch_bilgisi)
        self.roll_bilgisi = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.roll_bilgisi.setFrameShape(QtWidgets.QFrame.Box)
        self.roll_bilgisi.setText("")
        self.roll_bilgisi.setObjectName("roll_bilgisi")
        self.horizontalLayout_6.addWidget(self.roll_bilgisi)
        self.bir.addLayout(self.horizontalLayout_6)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 470, 161, 41))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.xyz_hizi_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.xyz_hizi_buton.setObjectName("xyz_hizi_buton")
        self.horizontalLayout_20.addWidget(self.xyz_hizi_buton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 529, 421, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.rtl_buton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.rtl_buton.setObjectName("rtl_buton")
        self.horizontalLayout_21.addWidget(self.rtl_buton)
        self.guided_buton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.guided_buton.setObjectName("guided_buton")
        self.horizontalLayout_21.addWidget(self.guided_buton)
        self.stabilize_buton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.stabilize_buton.setObjectName("stabilize_buton")
        self.horizontalLayout_21.addWidget(self.stabilize_buton)
        self.loiter_buton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.loiter_buton.setObjectName("loiter_buton")
        self.horizontalLayout_21.addWidget(self.loiter_buton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 261, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 280, 161, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 280, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 280, 81, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 570, 201, 31))
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(449, 530, 206, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_19.addWidget(self.pushButton_2)
        self.gorev2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.gorev2.setObjectName("gorev2")
        self.horizontalLayout_19.addWidget(self.gorev2)
        self.durum_cubugu = QtWidgets.QLabel(self.centralwidget)
        self.durum_cubugu.setGeometry(QtCore.QRect(10, 250, 561, 28))
        self.durum_cubugu.setFrameShape(QtWidgets.QFrame.Box)
        self.durum_cubugu.setText("")
        self.durum_cubugu.setObjectName("durum_cubugu")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(800)
        self.timer.timeout.connect(self.bilgi_yenileme_func)
        self.timer.start()
        self.counter = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.armed_buton.setText(_translate("MainWindow", "ARM"))
        self.x_hizi_buton.setText(_translate("MainWindow", "X HIZ"))
        self.y_hizi_buton.setText(_translate("MainWindow", "Y HIZ"))
        self.z_hizi_buton.setText(_translate("MainWindow", "Z HIZ"))
        self.yaw_buton.setText(_translate("MainWindow", "YAW"))
        self.pitch_buton.setText(_translate("MainWindow", "PITCH"))
        self.roll_buton.setText(_translate("MainWindow", "ROLL"))
        self.wp1_buton.setText(_translate("MainWindow", "WP1"))
        self.wp2_buton.setText(_translate("MainWindow", "WP2"))
        self.wp3_buton.setText(_translate("MainWindow", "WP3"))
        self.wp4_buton.setText(_translate("MainWindow", "WP4"))
        self.wp5_buton.setText(_translate("MainWindow", "WP5"))
        self.boylam.setText(_translate("MainWindow", "     BOYLAM"))
        self.enlem.setText(_translate("MainWindow", "      ENLEM   "))
        self.yukseklik.setText(_translate("MainWindow", " YUKSEKLIK"))
        self.mod.setText(_translate("MainWindow", "       MOD"))
        self.batarya.setText(_translate("MainWindow", "    BATARYA"))
        self.hiz.setText(_translate("MainWindow", "        HIZ"))
        self.yaw.setText(_translate("MainWindow", "       YAW"))
        self.pitch.setText(_translate("MainWindow", "      PİTCH"))
        self.roll.setText(_translate("MainWindow", "       ROLL"))
        self.xyz_hizi_buton.setText(_translate("MainWindow", "XYZ HIZ"))
        self.rtl_buton.setText(_translate("MainWindow", "RTL"))
        self.guided_buton.setText(_translate("MainWindow", "GUIDED"))
        self.stabilize_buton.setText(_translate("MainWindow", "STABILIZE"))
        self.loiter_buton.setText(_translate("MainWindow", "LOITER"))
        self.label.setText(_translate("MainWindow", "TELEMETRİ  BİLGİLERİ"))
        self.label_2.setText(_translate("MainWindow", "HIZLANMA KONTROLÜ"))
        self.label_3.setText(_translate("MainWindow", "AÇI KONTROLÜ"))
        self.label_4.setText(_translate("MainWindow", "WP ATAMA"))
        self.label_5.setText(_translate("MainWindow", "DESİGNED BY IHAMARMARA"))
        self.pushButton_2.setText(_translate("MainWindow", "Görev1"))
        self.gorev2.setText(_translate("MainWindow", "Görev2"))

        self.armed_buton.clicked.connect(self.arm_and_takeoff)

        self.wp1_buton.clicked.connect(self.wp1_func)
        self.wp2_buton.clicked.connect(self.wp2_func)
        self.wp3_buton.clicked.connect(self.wp3_func)
        self.wp4_buton.clicked.connect(self.wp4_func)
        self.wp5_buton.clicked.connect(self.wp5_func)

        self.x_hizi_buton.clicked.connect(self.x_hizi_func)
        self.y_hizi_buton.clicked.connect(self.y_hizi_func)
        self.z_hizi_buton.clicked.connect(self.z_hizi_func)
        self.xyz_hizi_buton.clicked.connect(self.xyz_hizi_func)
        self.yaw_buton.clicked.connect(self.yaw_func)
        self.pitch_buton.clicked.connect(self.pitch_func)
        self.roll_buton.clicked.connect(self.roll_func)
	
        self.guided_buton.clicked.connect(self.guided_func)
        self.rtl_buton.clicked.connect(self.rtl_func)
        self.stabilize_buton.clicked.connect(self.stabilize_func)
        self.loiter_buton.clicked.connect(self.loiter_func)

        self.pushButton_2.clicked.connect(self.gorev1)

		

		


    def bilgi_yenileme_func(self):
        
        self.enlem_bilgisi.setText(str(vehicle.location.global_frame.lat))
        self.boylam_bilgisi.setText(str(vehicle.location.global_frame.lon))
        self.yukseklik_bilgisi.setText(str(vehicle.location.global_frame.alt))
        self.mod_bilgisi.setText(str(vehicle.mode.name))
        self.batarya_bilgisi.setText(str(vehicle.battery.level))
        self.hiz_bilgisi.setText(str(vehicle.groundspeed))
        self.yaw_bilgisi.setText(str(vehicle.attitude.yaw*180/3.14159265359+360))
        self.pitch_bilgisi.setText(str(vehicle.attitude.pitch*180/3.14159265359))
        self.roll_bilgisi.setText(str(vehicle.attitude.roll*180/3.14159265359))
        self.durum_cubugu.setText(str(durumstr))



    def wp1_func(self):
		
        
        e1 = float(self.wp1_enlem_yazi_alani.text()) # enlemin e si 1.waypoint olduğuiçinde 1  
        
        b1 = float(self.wp1_boylam_yazi_alani.text()) # boylamın b si
		
	
        a1 = float(self.wp1_boylam_yazi_alani.text()) # altitude un a sı
        
        print("ilk wp gidiliyor")
        point1 = LocationGlobalRelative(e1, b1, a1)
        vehicle.simple_goto(point1,groundspeed=3)
        


    def wp2_func(self):
		
        
        e1 = float(self.wp2_enlem_yazi_alani.text()) # enlemin e si 1.waypoint olduğuiçinde 1  
        
        b1 = float(self.wp2_boylam_yazi_alani.text()) # boylamın b si
		
	
        a1 = float(self.wp2_boylam_yazi_alani.text()) # altitude un a sı
        
        print("ilk wp gidiliyor")
        point1 = LocationGlobalRelative(e1, b1, a1)
        vehicle.simple_goto(point1,groundspeed=10)
        

    def wp3_func(self):
		
        
        e1 = float(self.wp3_enlem_yazi_alani.text()) # enlemin e si 1.waypoint olduğuiçinde 1  
        
        b1 = float(self.wp3_boylam_yazi_alani.text()) # boylamın b si
		
	
        a1 = float(self.wp3_boylam_yazi_alani.text()) # altitude un a sı
        
        print("ilk wp gidiliyor")
        point1 = LocationGlobalRelative(e1, b1, a1)
        vehicle.simple_goto(point1)
        

    def wp4_func(self):
		
       
        e1 = float(self.wp4_enlem_yazi_alani.text()) # enlemin e si 1.waypoint olduğuiçinde 1  
        
        b1 = float(self.wp4_boylam_yazi_alani.text()) # boylamın b si
		
	
        a1 = float(self.wp4_boylam_yazi_alani.text()) # altitude un a sı
        
        print("ilk wp gidiliyor")
        point1 = LocationGlobalRelative(e1, b1, a1)
        vehicle.simple_goto(point1)
        

    def wp5_func(self):
		
        
        e1 = float(self.wp5_enlem_yazi_alani.text()) # enlemin e si 1.waypoint olduğuiçinde 1  
        
        b1 = float(self.wp5_boylam_yazi_alani.text()) # boylamın b si
		
	
        a1 = float(self.wp5_boylam_yazi_alani.text()) # altitude un a sı
        
        print("ilk wp gidiliyor")
        point1 = LocationGlobalRelative(e1, b1, a1)
        vehicle.simple_goto(point1)
        



    def x_hizi_func(self):
        
        velocity_x = float(self.x_hizi_yazi_alani.text())
        velocity_y = 0
        velocity_z = 0			
        msg = vehicle.message_factory.set_position_target_global_int_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, # lat_int - X Position in WGS84 frame in 1e7 * meters
        0, # lon_int - Y Position in WGS84 frame in 1e7 * meters
        0, # alt - Altitude in meters in AMSL altitude(not WGS84 if absolute or relative)
        # altitude above terrain if GLOBAL_TERRAIN_ALT_INT
        velocity_x, # X velocity in NED frame in m/s
        velocity_y, # Y velocity in NED frame in m/s
        velocity_z, # Z velocity in NED frame in m/s
        0, 0, 0, # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)

    	# send command to vehicle on 1 Hz cycle
        for x in range(0,10):
            vehicle.send_mavlink(msg)
            time.sleep(1)

    
    def y_hizi_func(self,y1):
        if y1 == 0:

            velocity_x = 0
            velocity_y = float(self.y_hizi_yazi_alani.text())
            velocity_z = 0
            iterasyon = 10	
        else :
            velocity_y = y1
            velocity_x = 0
            velocity_z = 0
            iterasyon = 4
        print("hız y")
        print(velocity_y)		
        msg = vehicle.message_factory.set_position_target_global_int_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, # lat_int - X Position in WGS84 frame in 1e7 * meters
        0, # lon_int - Y Position in WGS84 frame in 1e7 * meters
        0, # alt - Altitude in meters in AMSL altitude(not WGS84 if absolute or relative)
        # altitude above terrain if GLOBAL_TERRAIN_ALT_INT
        velocity_x, # X velocity in NED frame in m/s
        velocity_y, # Y velocity in NED frame in m/s
        velocity_z, # Z velocity in NED frame in m/s
        0, 0, 0, # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)

    	# send command to vehicle on 1 Hz cycle
        for x in range(0,iterasyon):
            vehicle.send_mavlink(msg)

    def z_hizi_func(self):
        
        velocity_x = 0
        velocity_y = 0
        velocity_z = float(self.z_hizi_yazi_alani.text())			
        msg = vehicle.message_factory.set_position_target_global_int_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, # lat_int - X Position in WGS84 frame in 1e7 * meters
        0, # lon_int - Y Position in WGS84 frame in 1e7 * meters
        0, # alt - Altitude in meters in AMSL altitude(not WGS84 if absolute or relative)
        # altitude above terrain if GLOBAL_TERRAIN_ALT_INT
        velocity_x, # X velocity in NED frame in m/s
        velocity_y, # Y velocity in NED frame in m/s
        velocity_z, # Z velocity in NED frame in m/s
        0, 0, 0, # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)

    	# send command to vehicle on 1 Hz cycle
        for x in range(0,10):
            vehicle.send_mavlink(msg)
            time.sleep(1)

    def xyz_hizi_func(self):
        
        velocity_x = float(self.x_hizi_yazi_alani.text())
        velocity_y = float(self.y_hizi_yazi_alani.text())
        velocity_z = float(self.z_hizi_yazi_alani.text())
        msg = vehicle.message_factory.set_position_target_global_int_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, # lat_int - X Position in WGS84 frame in 1e7 * meters
        0, # lon_int - Y Position in WGS84 frame in 1e7 * meters
        0, # alt - Altitude in meters in AMSL altitude(not WGS84 if absolute or relative)
        # altitude above terrain if GLOBAL_TERRAIN_ALT_INT
        velocity_x, # X velocity in NED frame in m/s
        velocity_y, # Y velocity in NED frame in m/s
        velocity_z, # Z velocity in NED frame in m/s
        0, 0, 0, # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)

    	# send command to vehicle on 1 Hz cycle
        for x in range(0,10):
            vehicle.send_mavlink(msg)
            time.sleep(1)

    def yaw_func(self,yaw1):
        print("yaw yaziliyor")
        print(self.yaw_yazi_alani.text())
        if yaw1 == 0:
            yaw = float(self.yaw_yazi_alani.text())
        
        else :
            yaw = yaw1
        print(yaw)
        is_relative = 1
        if(yaw<0):
            
            direction=0 #yaw relative to direction of travel
            yaw = yaw * -1
            print(yaw)
        else:
            direction = 1
        # create the CONDITION_YAW command using command_long_encode()
        msg = vehicle.message_factory.command_long_encode(
            0, 0,    # target system, target component
            mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
            0, #confirmation
            yaw,    # param 1, yaw in degrees
            0,          # param 2, yaw speed deg/s
            direction,          # param 3, direction -1 ccw, 1 cw
            is_relative, # param 4, relative offset 1, absolute angle 0
            0, 0, 0)    # param 5 ~ 7 not used
        # send command to vehicle
        vehicle.send_mavlink(msg)


    def pitch_func(self):
        pitch = float(self.pitch_yazi_alani.text())
        is_relative=1 #yaw relative to direction of travel

        # create the CONDITION_YAW command using command_long_encode()
        msg = vehicle.message_factory.command_long_encode(
            0, 0,    # target system, target component
            mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
            0, #confirmation
            pitch,    # param 1, yaw in degrees
            0,          # param 2, yaw speed deg/s
            1,          # param 3, direction -1 ccw, 1 cw
            is_relative, # param 4, relative offset 1, absolute angle 0
            0, 0, 0)    # param 5 ~ 7 not used
        # send command to vehicle
        vehicle.send_mavlink(msg)

    def roll_func(self):
        roll = float(self.roll_yazi_alani.text())
        is_relative=1 #yaw relative to direction of travel

        # create the CONDITION_YAW command using command_long_encode()
        msg = vehicle.message_factory.command_long_encode(
            0, 0,    # target system, target component
            mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
            0, #confirmation
            roll,    # param 1, yaw in degrees
            0,          # param 2, yaw speed deg/s
            1,          # param 3, direction -1 ccw, 1 cw
            is_relative, # param 4, relative offset 1, absolute angle 0
            0, 0, 0)    # param 5 ~ 7 not used
        # send command to vehicle
        vehicle.send_mavlink(msg)


    
    def guided_func(self):
	
        vehicle.mode = VehicleMode("GUIDED")
	
        vehicle.mode = VehicleMode("GUIDED")

    
    def rtl_func(self):
	
        vehicle.mode = VehicleMode("RTL")
	
        vehicle.mode = VehicleMode("RTL")

    def stabilize_func(self):
	
        vehicle.mode = VehicleMode("STABILIZE")
	
        vehicle.mode = VehicleMode("STABILIZE")

    def loiter_func(self):
	
        vehicle.mode = VehicleMode("LOITER")
	
        vehicle.mode = VehicleMode("LOITER")

    def arm_and_takeoff(self,alti):
    
    	
        #target_altitude = float(self.arm_yazi_alani.text())
        print(alti)
        target_altitude = float(alti)
        if alti ==0 :
            target_altitude = float(self.arm_yazi_alani.text())
        
        while not vehicle.is_armable:
            print(" Waiting for vehicle to initialise...")
            time.sleep(1)

        print("Arming motors")

        vehicle.mode = VehicleMode("GUIDED")
        vehicle.armed = True


        while not vehicle.armed:
            print(" Waiting for arming...")
            time.sleep(1)

        print("Taking off!")
        
        vehicle.simple_takeoff(target_altitude)  


        while True:
            print(" Altitude: ", vehicle.location.global_relative_frame.alt)

            
            if vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
                print("Reached target altitude")
                durumstr = "hedef yukseklige varildi"
                print(durumstr)
                break
            time.sleep(1)

    def uzaklik(self,lat1,lon1,lat2,lon2):
        dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180
        dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180
        a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) *math.sin(dLon/2) * math.sin(dLon/2)

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R * c
        d2= d* 1000
        return d2
			







    def advanced_goto(self,konumdizi) :
        
        konum1 = LocationGlobalRelative(konumdizi[0] ,konumdizi[1],konumdizi[2])
        vehicle.simple_goto(konum1)
        lat_now = vehicle.location.global_frame.lat
        lon_now = vehicle.location.global_frame.lon
        while(1):
            uzaklik_now = self.uzaklik(lat_now,lon_now,vehicle.location.global_frame.lat,vehicle.location.global_frame.lon)
            if uzaklik_now > 1:
                break
            else :
                vehicle.simple_goto(konum1,groundspeed=5)
                time.sleep(0.5)
                print("yeniden harekete geçiliyor")

        while (1):
            u1 =self.uzaklik(vehicle.location.global_frame.lat,vehicle.location.global_frame.lon,konumdizi[0],konumdizi[1])
            if u1 <2 :
                break
            else :
                print("konum" +str(konumdizi[3])+"e gidiliyor")
                durumstr = "konum" +str(konumdizi[3])+" e gidiliyor"
                time.sleep(0.8)
                if vehicle.mode.name != "GUIDED" :
                    vehicle.mode = VehicleMode("GUIDED")
                    vehicle.simple_goto(konum1)
        time.sleep(1)





    def kamera_func(self):
        kamera = cv2.VideoCapture(0)
        deger = 0
        global nokta_e  
        global nokta_b 
        while (1):
            print("kamera fonksiyonuna girdi")
            
            
            ret, image = kamera.read()
            blured = cv2.GaussianBlur(image, (15, 15), 0)
            hsv = cv2.cvtColor(blured, cv2.COLOR_BGR2HSV)
            lower = np.array([161, 155, 84])
            upper = np.array([179, 255, 255])
            mask = cv2.inRange(hsv, lower, upper)

            contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)

            for c in contours:
                area = cv2.contourArea(c)
                if area > 3000:
                    M = cv2.moments(c)
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
                    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
                    cv2.putText(image, "center", (cX - 20, cY - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    deger += 1
                    print(deger) 
            cv2.imshow("image",image)
            self.y_hizi_func(-1)
            if cv2.waitKey(25) & 0xFF == ord('q') :
                
                break
            if deger > 10:
                #kamera.relased
                nokta_e = vehicle.location.global_frame.lat
                nokta_b = vehicle.location.global_frame.lon
                vehicle.mode = VehicleMode("STABILIZE")
                vehicle.mode = VehicleMode("GUIDED")
                print("görev tamamlandı.")
                print("Bırakma noktası enlem :")
                print(nokta_e)
                print("Bırakma noktası boylam :")
                print(nokta_b)
                break
                 


    def gorev1(self):
        self.arm_and_takeoff(20)
        durumstr = "kalkış yapılıyor"
        konum_dizisi = [[40.9865192 ,29.0536673,10,1],
        [40.9864704 ,29.0545685,10,2],
        [40.9867956 ,29.0552015,25,3],
        [40.9873078 ,29.0546222,10,4],
        [40.9873891 ,29.0538068,10,5],
        [40.9874785 ,29.0529270,10,6],
        [40.9871045 ,29.0523798,10,7],
        [40.9866899 ,29.0527768,10,8]] 

        self.advanced_goto(konum_dizisi[1])
        self.advanced_goto(konum_dizisi[2])
        self.advanced_goto(konum_dizisi[3])

        yaw_son = vehicle.attitude.yaw*180/3.14159265359+360
        yaw_arti = 277-yaw_son
        if yaw_arti < 0:
            yaw_arti = 360-yaw_son + 277
        self.yaw_func(yaw_arti)
        print("yaw calisti")
        self.y_hizi_func(-1)

        self.kamera_func()
        self.advanced_goto(konum_dizisi[5])
        self.advanced_goto(konum_dizisi[6])
        self.advanced_goto(konum_dizisi[7])
        self.advanced_goto(konum_dizisi[0])

        print("görev tamamlandı.")
        print("Bırakma noktası enlem :")
        print(nokta_e)
        print("Bırakma noktası boylam :")
        print(nokta_b)
        durumstr ="enlem : " + str(nokta_e) +"boylam :"+str(nokta_b)
        vehicle.mode = VehicleMode("LAND")
        time.sleep(5000)


	

    def gorev2(self):
        pass
        
			




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
