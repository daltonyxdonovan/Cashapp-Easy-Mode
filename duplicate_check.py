import csv, time, sys, os
from datetime import datetime
from datetime import timedelta
import collections, functools, operator

cwd = os.getcwd()
now = datetime.now()
daysAgo = 90
ninetydaysago = now - timedelta(days=daysAgo)
flag = 0
itemlist = []
duplication_list = []
dictionary_num = {}
dictionary_price = {}

with open('cash_app_report.csv', encoding='utf-8-sig') as csvfile:
    time.sleep(.5)
    report = csv.reader(csvfile)
    next(report)
    for row in report:
        stripped = row[1].strip(' CD CST')
        datey = datetime.strptime(stripped, "%Y-%m-%d %H:%M:%S")
        if datey > ninetydaysago:
            
            if "-" in row[4]:
                duplication_list.append(row[11])
                dictionary_price[row[11]] = row[4]
                if row[11] not in itemlist:
                    itemlist.append(row[11])
            else:
                pass
    for item in itemlist:
        dictionary_num[item] = duplication_list.count(item)
    #write code to sort dictionary by value
    sorted_dictionary = sorted(dictionary_num.items(), key=lambda kv: kv[1], reverse=False)
    for item in sorted_dictionary:
        if item[1] > 1:
            if item[0] != "":
                print(str(item[0]).center(140))
                print("-----------------------------".center(140))
                print("times in the last 90 days:".center(140))
                print(str(item[1]).center(140))
                print("amount last spent:".center(140))
                print(str(dictionary_price[item[0]]).center(140))
                print("\n")
            else:
                print(str("CashApp Transfer").center(140))
                print("-----------------------------".center(140))
                print("times in the last 90 days:".center(140))
                print(str(item[1]).center(140))
                print("amount last spent:".center(140))
                print(str(dictionary_price[item[0]]).center(140))
                print("\n")
