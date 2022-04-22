import csv, time, shutil
from datetime import datetime
from datetime import timedelta
from colorama import init
init()
from colorama import Fore, Back
from os import system


with open("days.txt", "r") as f:
    daze = f.read()
    f.close

running = True
reading = False
alert = False
menu = True
updating = False
backdate = False
cals = False
dals = False
now = datetime.now()
days = timedelta(10)
income = 0
expense = 0
daze2 = 14
daze3 = 30
flag = 0

#dalton's variables
screen = (0,0,1920,10140)
search_dalton = (727,47)
dalton_login = (1496,178)
dalton_statements = (1845,267)
dalton_export = (1754,322)
def clear():
    print(chr(27) + "[2J")
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
clear()
tda = datetime.now() - timedelta(days=int(daze))
if flag == 0:
    try:
        with open('cash_app_report.csv', encoding='utf-8-sig') as csvfile:
            time.sleep(.5)
            report = csv.reader(csvfile)
            next(report)
            for row in report:
                stripped = row[1].strip(' CD CST')
                datey = datetime.strptime(stripped, "%Y-%m-%d %H:%M:%S")
                if datey > tda:
                    print(detectName(row).center(140))
                    if "-" in row[4]:
                        strip_row = row[4].replace(",", "")
                        print(stripped[0:10].center(140))
                        print(row[4].center(140))
                        expense = expense + float(strip_row.replace("$", ""))
                        print("\n")
                    else:
                        strip_row = row[4].replace(",", "")
                        print(stripped[0:10].center(140))
                        print(row[4].center(140))
                        income = income + float(strip_row.replace("$", ""))
                        print("\n")
            print("\n")
            print("\n")
            print("Income:".center(140))
            print(str(round(income, 2)).center(140))
            print("\n")
            print("Expenses:".center(140))
            print(str(round(expense, 2)).center(140))
            print("\n")
            print("Offset:".center(140))
            print(str(round(income + expense, 2)).center(140))
            print("\n")
            flag = 1
    except:
        print("doesn't work apparently -PLACEHOLDER-")