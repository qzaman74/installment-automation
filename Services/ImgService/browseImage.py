import os
from PyQt5.QtWidgets import QFileDialog
import base64

def getImagePath(parent):
    try:
        im_path = QFileDialog.getOpenFileName(parent,'Browse Image Window','./','Image Files(*.png)')
        path = im_path[0]
        if (os.path.exists(path)):
            file = open(path, 'rb')
            file_content = file.read()
            base64_code = base64.b64encode(file_content)
            return base64_code
    except:
        pass
