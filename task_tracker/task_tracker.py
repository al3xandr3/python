# needs envirnment variable PATH:
# "C:\Users\<user>\AppData\Local\Continuum\Anaconda\Library\bin"

# Running:
# c:\Users\amatos\AppData\Local\Continuum\Anaconda\pythonw.exe
# "%UserProfile%\Dropbox\my\projects\python\task_tracker\task_tracker.py"

import os
import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QListWidget
from PyQt4.QtGui import QListWidgetItem
import datetime
import pandas as pd
import numpy as np

# allow taskbar icon
import ctypes
myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# relative path of this script
app_path = os.path.dirname(os.path.realpath(__file__)) + "\\"


# return the last done tasks, by order of recency
def latest_tasks():
    raw = app_path + 'task_tracker.csv'
    data = pd.read_csv(raw, header=None, names=["timestamp", "task"])

    # timestamp as a datetime
    format = '%Y-%m-%d %H:%M:%S'
    data['timestamp'] = pd.to_datetime(data['timestamp'], format=format)

    latest = data[-60:]  # last weeks tasks

    groupby = latest.groupby(["task"])
    top = groupby.aggregate({'timestamp': [np.min, np.max]})
    top.columns = top.columns.droplevel(0)  # put the headers back
    top_sorted = top.sort_values(by="amax", ascending=False).head(n=15)
    return top_sorted


# create our window
app = QApplication(sys.argv)
app.setWindowIcon(QIcon(app_path + 'task_tracker.png'))
w = QWidget()
w.setWindowTitle('Task Tracker')


# Set window size.
w.resize(280, 230)

# Create textbox
textbox = QLineEdit(w)
textbox.move(20, 20)
textbox.resize(240, 30)

# Create a button in the window
button = QPushButton('Add', w)
button.move(20, 60)

# Create a button in the window
button_dir = QPushButton('data', w)
button_dir.move(170, 60)

# Create a button in the window
listWidget = QListWidget(w)
tasks = latest_tasks().index.tolist()
for i in tasks:
    item = QListWidgetItem("%s" % i)
    listWidget.addItem(item)
listWidget.resize(240, 115)
listWidget.move(20, 100)


@pyqtSlot()
def on_click_dir():
    import subprocess
    subprocess.call("start " + app_path, shell=True)


@pyqtSlot()
def on_click_choice(curr):
    textbox.setText(curr.text())


# Create the actions
@pyqtSlot()
def on_click():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = str(textbox.text()).upper()
    if task == "":
        QMessageBox.information(w, "Uops...", "Please insert a Task")
    else:
        row = "\n%s,%s" % (now, task)
        fd = open(app_path + 'task_tracker.csv', 'a')
        fd.write(row)
        fd.close()
        app.exit()

# connect the signals to the slots
button.clicked.connect(on_click)
button_dir.clicked.connect(on_click_dir)
textbox.returnPressed.connect(on_click)  # accept enter instead
listWidget.currentItemChanged.connect(on_click_choice)
# Show the window and run the app
w.show()
app.exec_()
