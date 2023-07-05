

import json
import sys

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication


class CloudWindow(QMainWindow):

    def __init__(self):
        super(CloudWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(464, 257)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 60, 111, 61))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 60, 101, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 60, 41, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 100, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 100, 41, 31))
        self.label_4.setObjectName("label_4")
        self.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setWindowTitle("MainWindow")
        self.pushButton.setText("读取")
        self.label.setText("TextLabel")
        self.label_2.setText("温度")
        self.label_3.setText("TextLabel")
        self.label_4.setText("湿度")
        self.pushButton.clicked.connect(self.btnClick)
        self.Token = ""

    def btnClick(self):
        r = requests.post(""http://云平台地址/Users/Login", data={"Account": "【username】", "Password": "【password】", "IsRememberMe": "true"})
        self.Token = json.loads(r.text)["ResultObj"]["AccessToken"]
        r = requests.get("http://云平台地址/devices/设备ID/sensors/设备标识", headers={"AccessToken": self.Token})
        sensor = json.loads(r.text)["ResultObj"]['Value']
        self.label.setText(str(sensor))
        r = requests.get("http://云平台地址/devices/设备ID/sensors/设备标识", headers={"AccessToken": self.Token})
        sensor = json.loads(r.text)["ResultObj"]['Value']
        self.label_3.setText(str(sensor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CloudWindow()
    window.show()
    sys.exit(app.exec_())
