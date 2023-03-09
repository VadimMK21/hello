import sys
import sqlite3;
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load("widget.ui", None)

con = sqlite3.connect("granit.sqlite3")

cursor = con.cursor()

def load_data() :

    if window.checkBox_1.isChecked():
        cursor.execute("SELECT * FROM granit WHERE FA = 'ТС'")
        window.checkBox_2.setChecked(True)
        for person in cursor.fetchall():

            window.textBrowser.append('{0}_{1}_{2:<2}{3}{4:25}{5}{6}'.format(person[0], person[1], person[2], '\t', person[8], '\t', person[11]))

    else:
        window.checkBox_2.setChecked(False)
        window.textBrowser.setText("")

def find_data() :
    window.textBrowser.clear()
    find_text = window.lineEdit.text()
    cursor.execute(f"SELECT * FROM granit WHERE FA = 'ТС' AND IMJ LIKE '%{find_text}%'")
    window.checkBox_2.setChecked(True)
    for person in cursor.fetchall():

        window.textBrowser.append('{0}_{1}_{2:<2}{3}{4:25}{5}{6}'.format(person[0], person[1], person[2], '\t', person[8], '\t', person[11]))

window.pushButton.clicked.connect(load_data)
window.findButton.clicked.connect(find_data)
#window.lineEdit.keyPressEvent(self, event)
window.show()
app.exec()