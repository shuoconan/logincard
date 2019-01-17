import base64
import json
import os
from PyQt5.QtWidgets import QComboBox, QMessageBox
import requests
from Crypto.Cipher import AES
from xml.dom import minidom as xmldom
import time
class custom_combox(QComboBox):
    def __init__(self,parent = None):
        super(custom_combox,self).__init__(parent)
    def showPopup(self):
        self.clear()


