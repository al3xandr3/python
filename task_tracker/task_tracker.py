# needs envirnment variable PATH:"C:\Users\<user>\AppData\Local\Continuum\Anaconda\Library\bin"

# c:\Users\amatos\AppData\Local\Continuum\Anaconda\pythonw.exe 
#"%UserProfile%\Dropbox\my\projects\python\task_tracker\task_tracker.py"

import os
import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
import datetime

# allow taskbar icon
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

## relative path of this script
app_path = os.path.dirname(os.path.realpath(__file__)) + "\\"


# create our window
app = QApplication(sys.argv)
app.setWindowIcon(QIcon(app_path + 'task_tracker.png'))
w   = QWidget()
w.setWindowTitle('Task Tracker')

# Create textbox
textbox = QLineEdit(w)
textbox.move(20, 20)
textbox.resize(240,30)

# Set window size.	
w.resize(280, 100)
 
# Create a button in the window
button = QPushButton('Add', w)
button.move(20,60)

# Create a button in the window
button_dir = QPushButton('data', w)
button_dir.move(170,60)

@pyqtSlot()
def on_click_dir():
	import subprocess
	subprocess.call("start " + app_path, shell=True)
 
# Create the actions 
@pyqtSlot()
def on_click():
	now  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	task = textbox.text()
	if task == "":
		QMessageBox.information(w, "Uops...", "Please insert a Task")
	else:
		row = "\n%s,%s" % (now, task)
		fd = open(app_path + 'task_tracker.csv','a')
		fd.write(row)
		fd.close()
		app.exit()

# connect the signals to the slots
button.clicked.connect(on_click)
button_dir.clicked.connect(on_click_dir)
textbox.returnPressed.connect(on_click) # accept enter instead
# Show the window and run the app
w.show()
app.exec_()