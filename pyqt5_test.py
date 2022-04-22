
from PyQt5.QtWidgets import (QPushButton, QRadioButton, QPlainTextEdit, QGridLayout, QWidget)
from PyQt5.QtCore import QProcess
from qtpy import QtWidgets
from PyQt5.QtGui import QFont
import sys, re, os, qdarkstyle, csv, time
from datetime import datetime
from datetime import timedelta

os.environ['QT_API'] = 'pyqt5'
progress_re = re.compile("Total complete: (\d+)%")

reading = False
alert = False
menu = True
updating = False
backdate = False
cals = False
dals = False
cwd = os.getcwd()
now = datetime.now()
days = timedelta(10)
income = 0
expense = 0
daze2 = 14
daze3 = 30
flag = 0
daze = 0

def writeToDays(days):
    if "day_variable.txt" in cwd:
        os.remove("day_variable.txt")
        with open("day_variable.txt", "w") as day_variable:
            day_variable.write(days)
            day_variable.close()
def reading_it():
    global flag
    global daze
    tda = datetime.now() - timedelta(days=int(daze))
    if flag == 0:
        try:
            with open('cash_app_report.csv', encoding='utf-8-sig') as csvfile:
                report = csv.reader(csvfile)
                next(report)
                for row in report:
                    stripped = row[1].strip(' CD CST')
                    datey = datetime.strptime(stripped, "%Y-%m-%d %H:%M:%S")
                    if datey > tda:
                        time.sleep(.1)
                        print(detectName(row).center(180))
                        if "-" in row[4]:
                            strip_row = row[4].replace(",", "")
                            print(stripped[0:10].center(180))
                            print(row[4].center(180))
                            expense = expense + float(strip_row.replace("$", ""))
                            print("\n")
                        else:
                            strip_row = row[4].replace(",", "")
                            print(stripped[0:10].center(180))
                            print(row[4].center(180))
                            income = income + float(strip_row.replace("$", ""))
                            print("\n")
                print("Income:".center(180))
                print(str(round(income, 2)).center(180))
                print("\n")
                print("Expenses:".center(180))
                print(str(round(expense, 2)).center(180))
                print("\n")
                print("Offset:".center(180))
                print(str(round(income + expense, 2)).center(180))
                print("\n")
                flag = 1
        except:
            print("doesn't work apparently -PLACEHOLDER-")
def detectName(rows):
    if "rent" in rows[11] or "Rent" in rows[11]:
        return str("Rent")
    elif "Google" in rows[11]:
        return str("Google")
    elif "Spotify" in rows[11]:
        return str("Spotify")
    elif "EDUCATION" in rows[11]:
        return str("Typing Class")
    elif "Pandora" in rows[11]:
        return str("Pandora")
    elif "Youtube" in rows[11]:
        return str("TV")
    elif "Netflix" in rows[11] or "NETFLIX" in rows[11]:
        return str("TV")
    elif "Amazon" in rows[11] or "AMZN" in rows[11] or "AMAZON" in rows[11]:
        return str("Amazon")
    elif "SLIDE" in rows[11] or "Speedway" in rows[11] or "GAS" in rows[11]:
        return str("Gas Station")
    elif "SUPERCENTER" in rows[11] or "WALMART" in rows[11] or "Wal-Mart" in rows[11] or "WAL-MART" in rows[11]:
        return str("Walmart")
    elif "Hulu" in rows[11]:
        return str("Hulu")
    elif "Etsy" in rows[11]:
        return str("Etsy")
    elif "Patreon" in rows[11]:
        return str("Patreon")
    elif "Ortonville" in rows[11]:
        return str("Storage")
    elif "Microsoft" in rows[11]:
        return str("Microsoft")
    elif "UBER " in rows[11] or "Uber" in rows[11] or "UBR" in rows[11]:
        return str("Uber Eats")
    elif "PROG" in rows[11]:
        return str("Car Insurance")
    elif "FUNIMATION" in rows[11]:
        return str("TV")
    elif "SPECTRUM" in rows[11]:
        return str("Internet")
    elif "NINTENDO" in rows[11]:
        return str("Nintendo")
    elif "XCEL" in rows[11]:
        return str("Electricity and Gas")
    elif "FIELD NATION" in rows[11]:
        return str("Field Nation")
    elif "ABCMOUSE" in rows[11]:
        return str("ABCMouse")
    elif "CHASE" in rows[11]:
        return str("Credit card")
    elif "PARAMOUNT" in rows[11]:
        return str("TV")
    elif "Water" in rows[11] or "water" in rows[11]:
        return str("Water")
    elif "AARON" in rows[11]:
        return str("Aarons")
    elif "LEEANN" in rows[11]:
        return str("Leeann Chins")
    elif "SHUTTERFLY" in rows[11]:
        return str("Shutterfly")
    elif "PIZZA HUT" in rows[11]:
        return str("Pizza Hut")
    elif "DOORDASH" in rows[11]:
        return str("DoorDash")
    elif "TREAS" in rows[11]:
        return str("IRS")
    elif "CRICKET" in rows[11]:
        return str("Phones")
    elif "TWITCH" in rows[11]:
        return str("Twitch")
    elif rows[11] == "" and rows[12] != "":
        return str("CashApp")
    else:
        return str("CashApp")
def clear():
    print(chr(27) + "[2J")
def simple_percent_parser(output):
    """
    Matches lines using the progress_re regex,
    returning a single integer for the % progress.
    """
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)

class Example(QWidget):
    def onPressed(self):
        pass
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Cash.App Reporting Tool                                     I love you baby <3')
        self.p = None
        self.setGeometry(650, 30, 620, 1000)

        #textbox
        self.textbox = QPlainTextEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.setFont(QFont("Sans Serif", 10))
        self.setGeometry(650, 30, 620, 1000)
        self.textbox.setStyleSheet("background-color: #000000; color: #ffffff;")

        #read button
        self.button_read = QPushButton('Print Report', self)
        self.button_read.setToolTip('Reads out times, amounts, and descriptions')
        self.button_read.setFont(QFont("Sans Serif", 10))
        self.button_read.clicked.connect(self.read_csv)

        #scan button
        self.button_scan = QPushButton('Scan Due Dates', self)
        self.button_scan.setToolTip('Scan for almost due bills')
        self.button_scan.setFont(QFont("Sans Serif", 10))
        self.button_scan.clicked.connect(self.read_alert)

        #download button
        self.button_download = QPushButton('Download Report', self)
        self.button_download.setToolTip('Download an updated report <b>***DO NOT TOUCH MOUSE OR KEYBOARD UNTIL SCRIPT COMPLETES***<b>')
        self.button_download.setFont(QFont("Sans Serif", 10))
        self.button_download.clicked.connect(self.doownload)

        #repeats button
        self.button_backdate = QPushButton('Repeats-Check', self)
        self.button_backdate.setToolTip('Checks for repeating transactions')
        self.button_backdate.setFont(QFont("Sans Serif", 10))
        self.button_backdate.clicked.connect(self.recurring)

        #radio buttons
        self.radio_button_1 = QRadioButton('1 Day', self)
        self.radio_button_1.setFont(QFont("Sans Serif", 10))
        self.radio_button_1.setChecked(False)
        self.radio_button_1.toggled.connect(self.on_radio_button1_toggled)
        self.radio_button_7 = QRadioButton('7 Days', self)
        self.radio_button_7.setFont(QFont("Sans Serif", 10))
        self.radio_button_7.setChecked(False)
        self.radio_button_7.toggled.connect(self.on_radio_button7_toggled)
        self.radio_button_14 = QRadioButton('14 Days', self)
        self.radio_button_14.setFont(QFont("Sans Serif", 10))
        self.radio_button_14.setChecked(False)
        self.radio_button_14.toggled.connect(self.on_radio_button14_toggled)
        self.radio_button_30 = QRadioButton('30 Days', self)
        self.radio_button_30.setFont(QFont("Sans Serif", 10))
        self.radio_button_30.setChecked(False)
        self.radio_button_30.toggled.connect(self.on_radio_button30_toggled)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.radio_button_1, 1, 1)
        grid.addWidget(self.radio_button_7, 1, 2)
        grid.addWidget(self.radio_button_14, 1, 3)
        grid.addWidget(self.radio_button_30, 1, 4)
        grid.addWidget(self.button_read, 2, 1)
        grid.addWidget(self.button_scan, 2, 2)
        grid.addWidget(self.button_download, 2, 3)
        grid.addWidget(self.button_backdate, 2, 4)
        grid.addWidget(self.textbox, 3, 1, 4, 4)
        self.setLayout(grid)
        self.show()
    def on_radio_button1_toggled(self):
        if "days.txt" in cwd:
            os.remove("days.txt")
        with open("days.txt", "w") as f:
            f.write('1')
            f.close
    def on_radio_button7_toggled(self):
        if "days.txt" in cwd:
            os.remove("days.txt")
        with open("days.txt", "w") as f:
            f.write('7')
            f.close
    def on_radio_button14_toggled(self):
        if "days.txt" in cwd:
            os.remove("days.txt")
        with open("days.txt", "w") as f:
            f.write('14')
            f.close
    def on_radio_button30_toggled(self):
        if "days.txt" in cwd:
            os.remove("days.txt")
        with open("days.txt", "w") as f:
            f.write('30')
            f.close
    def recurring(self):
        self.textbox.clear()
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.setGeometry(650, 30, 620, 1000)
            self.p.start("python", ['duplicate_check.py'])
    def read_csv(self):
        self.textbox.clear()
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.setGeometry(650, 30, 620, 1000)
            self.p.start("python", ['readery.py'])
    def doownload(self):
        self.textbox.clear()
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("python", ['redownload.py'])
    def message(self, s):
        self.textbox.appendPlainText(s)
    def read_alert(self):
        self.textbox.clear()
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("python", ['alerting.py'])
    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        # Extract progress if it is in the data.
        progress = simple_percent_parser(stderr)
        if progress:
            self.progress.setValue(progress)
        self.message(stderr)
    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)
    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Stopping',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running!',
        }
        state_name = states[state]
        self.message(f"*{state_name}*".center(65, '='))
    def process_finished(self):
        self.p = None

#MAIN LOOP
def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ex = Example()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()