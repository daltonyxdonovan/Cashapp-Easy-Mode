import csv, os, sys, subprocess, time, shutil, pyautogui, PySimpleGUI as sg
from datetime import datetime
from datetime import timedelta
from colorama import init
from PIL import ImageTk, Image
init()
from colorama import Fore, Back
from os import system

running = True
reading = False
alert = False
menu = True
updating = False
backdate = False
cals = False
dals = True

login = "login.png"
now = datetime.now()
days = timedelta(10)
income = 0
expense = 0
daze = 0
daze2 = 14
daze3 = 30
flag = 0
search = (809,101)
x = (0,20,1900,0)

cal_screen = (0,0,2560,1440)
alert_list = []
alert_list2 = []
master_list = ['Rent', 'Storage', 'Car insurance', 'Internet', 'Electricity/Gas', 'Credit Card', 'Water', 'Phones']

#dalton's variables
screen = (0,0,1920,1080)
search_dalton = (727,47)
dalton_login = (1496,178)
dalton_statements = (1845,275)
dalton_export = (1754,322)
cal_export = (2407,165)
cal_statement = (2512,103)
cal_login = (1822,119)
def update_script():
    if dals == True:
        time.sleep(5)
        subprocess.call(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "/max"])
        pyautogui.getWindowsWithTitle("New Tab")[0].maximize()
        time.sleep(5)
        pyautogui.tripleClick(search_dalton[0],search_dalton[1])
        pyautogui.typewrite("cash.app")
        pyautogui.press("enter")
        time.sleep(10)
        pyautogui.click(dalton_login[0],dalton_login[1])
        time.sleep(5)
        pyautogui.click(dalton_statements[0],dalton_statements[1])
        time.sleep(2)
        pyautogui.click(dalton_export[0],dalton_export[1])
        time.sleep(10)
        pyautogui.click(1900, 10)
    if cals == True:
        time.sleep(5)
        subprocess.call(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "/max"])
        pyautogui.getWindowsWithTitle("New Tab")[0].maximize()
        time.sleep(5)
        pyautogui.tripleClick(search)
        pyautogui.typewrite("cash.app")
        pyautogui.press("enter")
        time.sleep(5)
        login_button = pyautogui.locateOnScreen(login, screen, confidence=0.5)
        pyautogui.click(cal_login)
        time.sleep(2)
        statements = pyautogui.locateOnScreen("statements.png", screen, confidence=0.5)
        pyautogui.click(cal_statement)
        time.sleep(2)
        export = pyautogui.locateOnScreen("export.png", screen, confidence=0.5)
        pyautogui.click(cal_export)
        time.sleep(5)
        pyautogui.click(x)

cwd = os.getcwd()
if "cash_app_report.csv" in os.listdir(cwd):
    os.remove("cash_app_report.csv")
    print(Fore.GREEN + "Report in current directory has been removed.".center(140))
try:
    os.remove("c:/Users/dalto/Downloads/cash_app_report.csv")
    print(Fore.GREEN + "Removed report from Dalton's Downloads folder.".center(140))
    dals = True
    cals = False
except:
    print(Fore.RED + "Can't remove report from Dalton's Downloads folder.".center(140))
try:
    os.remove("c:/Users/calli/Downloads/cash_app_report.csv")
    print(Fore.GREEN + "Removed report from Cal's Downloads folder.".center(140))
    cals = True
    dals = False
except:
    print(Fore.RED + "Can't remove report from Cal's Downloads folder.".center(140))

update_script()
###################################put the code to download the report here, and reorder the logic to make it delete old one in downloads first##############################################
try:
    shutil.copy("c:/Users/calli/Downloads/cash_app_report.csv", cwd)
    print(Fore.GREEN + "Copied Cal's report to current directory from Downloads.".center(140))
except:
    print(Fore.RED + "Cannot copy Cal's report. If you're Cal, is it in Downloads?".center(140))           
try:
    shutil.copy("c:/Users/dalto/Downloads/cash_app_report.csv", cwd)
    print(Fore.GREEN + "Copied Dalton's report to current directory from Downloads.".center(140))
except:
    print(Fore.RED + "Cannot copy Dalton's report. If you're Dalton, is it in Downloads?".center(140))
print(Fore.CYAN +  "\n")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencv-python', 'colorama', 'datetime', 'pyautogui'])
reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).center(140)
print("\n")
print("Finished moving required files and updating required packages.".center(140))
print("\n")
time.sleep(5)

menu = True
updating = False
