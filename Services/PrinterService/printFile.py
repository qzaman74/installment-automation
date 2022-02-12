from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport



def makeTableDocument(tbl):
    document = QtGui.QTextDocument()
    cursor = QtGui.QTextCursor(document)
    rows = tbl.rowCount()
    columns = tbl.columnCount()
    table = cursor.insertTable(rows + 1, columns)
    format = table.format()
    format.setHeaderRowCount(1)
    table.setFormat(format)

    format = cursor.blockCharFormat()
    format.setFontWeight(QtGui.QFont.Bold)
    for column in range(columns):
        cursor.setCharFormat(format)
        cursor.insertText(
            tbl.horizontalHeaderItem(column).text())
        cursor.movePosition(QtGui.QTextCursor.NextCell)

    for row in range(rows):
        for column in range(columns):

            cursor.insertText(tbl.model().index(row, column).data())
            #print(tbl.itemAt(row,column).text())
            cursor.movePosition(QtGui.QTextCursor.NextCell)

    return document


def handlePaintRequest(printer,table):
    document = makeTableDocument(table)
    document.print_(printer)


def printTable(table):
    dialog = QtPrintSupport.QPrintDialog()
    dialog.printer().setPageSize(dialog.printer().Legal)
    dialog.printer().setDocName(QtCore.QCoreApplication.translate("Optim Softwares","Sale Report"))
    dialog.printer().setPaperSource(dialog.printer().Middle)
    dialog.printer().setFullPage(True)
    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        handlePaintRequest(dialog.printer(),table)


#####3
# import sys
# from PyQt4.QtGui import *
#
# class Widget(QWidget):
#     def paintEvent(self, event):
#         p = QPainter()
#         p.begin(self)
#
#         # Draw a 2cm x 2cm square.
#         width = self.logicalDpiX() * 2 / 2.54
#         height = self.logicalDpiY() * 2 / 2.54
#         p.drawRect(10, 10, width, height)
#
#         p.end()

# app = QApplication(sys.argv)
# w = Widget()
# w.show()
# sys.exit(app.exec_())
