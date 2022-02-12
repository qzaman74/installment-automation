import base64
from PyQt5.QtGui import QPixmap
        
def getPixmap(base64Code):
    img = base64.b64decode(base64Code)
    filename = 'decoded_image.png'  # I assume you have a way of picking unique filename
    with open(filename, 'wb') as f:
        f.write(img)
        f.flush()
        f.close()
    pixmap = QPixmap(filename)
    return pixmap
