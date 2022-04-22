import csv, os, sys, subprocess, time, shutil, pyautogui, PySimpleGUI as sg
from datetime import datetime
from datetime import timedelta
from colorama import init
init()
from colorama import Fore, Back
from os import system
daze2 = 14
daze3 = 30

alert_list = []
alert_list2 = []
master_list = ['Rent', 'Storage', 'Car insurance', 'Internet', 'Electricity/Gas', 'Credit Card', 'Water', 'Phones']

def diff(list1):
    return list(set(list1) - set(master_list)) + list(set(master_list) - set(list1))
def Alerts(rows):
    if "rent" in rows[11] or "Rent" in rows[11]:
        alert_list.append("Rent")
    elif "Ortonville" in rows[11]:
        alert_list.append("Storage")
    elif "PROG" in rows[11]:
        alert_list.append("Car insurance")
    elif "SPECTRUM" in rows[11]:
        alert_list.append("Internet")
    elif "XCEL" in rows[11]:
        alert_list.append("Electricity/Gas")
    elif "CHASE" in rows[11]:
        alert_list.append("Credit Card")
    elif "Water" in rows[11] or "water" in rows[11]:
        alert_list.append("Water")
    elif "CRICKET" in rows[11]:
        alert_list.append("Phones")

def clear():
    print(chr(27) + "[2J")

def Alerts2(rows):
    if "rent" in rows[11] or "Rent" in rows[11]:
        alert_list2.append("Rent")
    elif "Ortonville" in rows[11]:
        alert_list2.append("Storage")
    elif "PROG" in rows[11]:
        alert_list2.append("Car insurance")
    elif "SPECTRUM" in rows[11]:
        alert_list2.append("Internet")
    elif "XCEL" in rows[11]:
        alert_list2.append("Electricity/Gas")
    elif "CHASE" in rows[11]:
        alert_list2.append("Credit Card")
    elif "Water" in rows[11] or "water" in rows[11]:
        alert_list2.append("Water")
    elif "CRICKET" in rows[11]:
        alert_list2.append("Phones")


tda2 = datetime.now() - timedelta(days=daze2)
tda3 = datetime.now() - timedelta(days=daze3)
with open('cash_app_report.csv', encoding='utf-8-sig') as csvfile:
    report = csv.reader(csvfile)
    next(report)
    for row in report:
        stripped = row[1].strip(' CD CST')
        datey = datetime.strptime(stripped, "%Y-%m-%d %H:%M:%S")
        if datey > tda2:
            
            Alerts(row)
        if datey > tda3:
            Alerts2(row)
    clear()
    print("\n")
    print(Fore.YELLOW + "Two-week warning:".center(140))
    print(Fore.YELLOW + str(diff(alert_list)).center(140))
    print("\n")
    print(Fore.RED + "30-day warning:".center(140))
    print(Fore.RED + str(diff(alert_list2)).center(140))
    print("\n")