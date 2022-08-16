# -*- coding: utf-8 -*-
from asyncore import write
import time
import requests
import urllib3
import os
urllib3.disable_warnings()

url = "https://api.p2pquake.net/v1/human-readable?limit=1"

data = requests.get(url, verify=False).json()[0]

if data["code"] != (551):
    exit()
#判定資料是否為地震情報(震源情報、震度速報等)

logfile = open('log.txt', encoding="utf8")
logid1 = logfile.read()
logfile.close
#讀取上次情報ID
logid2 = data["_id"]["$oid"]
#讀取此次情報ID


if logid1 == logid2:
    exit()
#判定資料是否為重複


eq = data["earthquake"]
津波情報 = eq["domesticTsunami"]
深さ = (eq["hypocenter"]["depth"]).replace("km","キロ")
規模 = eq["hypocenter"]["magnitude"]
震源地= eq["hypocenter"]["name"]
最大震度 = eq["maxScale"]
発生日時 = eq["time"]
情報種類 = data["issue"]["type"]
震度 = data["points"]

#變數

if 最大震度 == 10:
    最大震度 = ("１")
elif 最大震度 == 20:
    最大震度 = ("２")
elif 最大震度 == 30:
    最大震度 = ("３")
elif 最大震度 == 40:
    最大震度 = ("４")
elif 最大震度 == 45:
    最大震度 = ("５弱")
elif 最大震度 == 46:
    最大震度 = ("５弱以上と推定")
elif 最大震度 == 50:
    最大震度 = ("５強")
elif 最大震度 == 55:
    最大震度 = ("６弱")
elif 最大震度 == 60:
    最大震度 = ("６強")
elif 最大震度 == 70:
    最大震度 = ("７")
#判定最大震度


if 規模 == "-1.0":
    規模 = "不明"

    

if 津波情報 == "None":
    津波情報 = "この地震による津波の心配はありません"
elif 津波情報 == "Unknown":
    津波情報 = "津波情報不明"
elif 津波情報 == "Checking":
    津波情報 = "津波の有無を調查中　念のため津波に注意してください"
elif 津波情報 == "NonEffective":
    津波情報 = "多少の潮位変動があるかもしれません　被害の心配はありません"
elif 津波情報 == "Watch":
    津波情報 = "津波注意報が発表中　海岸から離れてください "
elif 津波情報 == "Warning":
    津波情報 = "津波警報等が発表中　直ちに高台に避難してください"
#判定海嘯情報種類

a=0
name = ""
for i in 震度:
    if (震度[a]["scale"]) == 70:
        name = name + 震度[a]["addr"] + "　"
    a=a+1
snd7 = "＜震度７＞" + name[0:-1]
a=0
name = ""

for i in 震度:
    if (震度[a]["scale"]) == 60:
        name = name + 震度[a]["addr"] + "　"
    a=a+1
snd6t = "＜震度６強＞" + name[0:-1]
a=0
name = ""

for i in 震度:
    if (震度[a]["scale"]) == 55:
        name = name + 震度[a]["addr"] + "　"
    a=a+1
snd6j = "＜震度６弱＞" + name[0:-1]
a=0
name = ""

for i in 震度:
    if (震度[a]["scale"]) == 50:
        name = name + 震度[a]["addr"] + "　"
    a=a+1
snd5t = "＜震度５強＞" + name[0:-1]
a=0
name = ""

for i in 震度:
    if (震度[a]["scale"]) == 45:
        name = name + 震度[a]["addr"] + "　"
    a=a+1
snd5j = "＜震度５弱＞" + name[0:-1]
a=0
name = ""

for i in 震度:
    if (震度[a]["scale"]) == 46:
        name = name + 震度[a]["addr"] + "　"
    a=a+1
snd5s = "＜推定５弱以上＞" + name[0:-1]
a=0
name = ""

for i in 震度:
    if (震度[a]["scale"]) == 40:
        name = name + 震度[a]["addr"] + "　"
    a=a+1
snd4 = "＜震度４＞" + name[0:-1]
a=0
name = ""

for i in 震度:
    if (震度[a]["scale"]) == 30:
        name = name + 震度[a]["addr"] + "　"
    a=a+1
snd3 = "＜震度３＞" + name[0:-1]
a=0
name = ""

for i in 震度:
    if (震度[a]["scale"]) == 20:
        name = name + 震度[a]["addr"] + "　"
    a=a+1
snd2 = "＜震度２＞" + name[0:-1]
a=0
name = ""

for i in 震度:
    if (震度[a]["scale"]) == 10:
        name = name + 震度[a]["addr"] + "　"
    a=a+1
snd1 = "＜震度１＞" + name[0:-1]
a=0
name = ""

'''
print(snd7)
print(snd6t)
print(snd6j)
print(snd5t)
print(snd5j)
print(snd5s)
print(snd4)
print(snd3)
print(snd2)
print(snd1)
'''

f = open("log.txt", "w",encoding="utf8")
f.write(data["_id"]["$oid"])
f.close()
#寫入情報ID

'''
情報種類
    ScalePrompt 震度速報
    Destination 震源に関する情報
    ScaleAndDestination 震度・震源に関する情報
    DetailScale 各地の震度に関する情報
    Foreign 遠地地震に関する情報
    Other その他の情報
'''


for i in range(5):

    if 情報種類 == ("DetailScale"):
        #地震情報(各地の震度)
        print("地震情報")

        output = ("【地震情報】" + 発生日時 + "頃　最大震度" + 最大震度 + "の地震がありました")
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()

        output = (津波情報)
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()

        output = ("震源は" + 震源地 + "　深さ" + 深さ + "　マグニッチュード" + 規模)
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()

    elif 情報種類 == ("ScaleAndDestination"):
        #地震情報(各地の震度)
        print("地震情報")

        output = ("【地震情報】" + 発生日時 + "頃　最大震度" + 最大震度 + "の地震がありました")
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()

        output = (津波情報)
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()

        output = ("震源は" + 震源地 + "　深さ" + 深さ + "　マグニッチュード" + 規模)
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()

    elif 情報種類 == ("Destination"):
        #震源情報
        print("震源情報")

        output = ("【震源情報】" + 発生日時 + "頃地震がありました")
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()

        output = (津波情報)
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()

        output = ("震源は" + 震源地 + "　深さ" + 深さ + "　マグニッチュード" + 規模)
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()


    elif 情報種類 == ("ScalePrompt"):
        #震度速報
        print("震度速報")

        output = ("【震度速報】" + 発生日時 + "頃　最大震度" + 最大震度 + "の地震がありました")
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()

    elif 情報種類 == ("Foreign"):
        #遠地地震
        print("遠地地震")

        output = ("【遠地地震】" + 発生日時 + "頃地震がありました")
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)
        
        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()

        output = (津波情報)
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()

        output = ("震源は" + 震源地 + "　深さ" + 深さ + "　マグニッチュード" + 規模)
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()


    #震度7
    if snd7 != "＜震度７＞":

        length = 0
        for i in snd7:
            length+=1
        #判定情報字數
        row = length//36+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = snd7[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            print("7")
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid3 != logid2:
                exit()

    #震度6強
    if snd6t != "＜震度６強＞":

        length = 0
        for i in snd6t:
            length+=1
        #判定情報字數
        row = length//36+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = snd6t[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            print("6+")
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid3 != logid2:
                exit()

    #震度6弱
    if snd6j != "＜震度６弱＞":

        length = 0
        for i in snd6j:
            length+=1
        #判定情報字數
        row = length//36+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = snd6j[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            print("6-")
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid3 != logid2:
                exit()

    #震度5強
    if snd5t != "＜震度５強＞":

        length = 0
        for i in snd5t:
            length+=1
        #判定情報字數
        row = length//36+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = snd5t[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            print("5+")
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid3 != logid2:
                exit()

    #震度5弱
    if snd5j != "＜震度５弱＞":

        length = 0
        for i in snd5j:
            length+=1
        #判定情報字數
        row = length//36+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = snd5j[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            print("5-")
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid3 != logid2:
                exit()

    #推定震度5弱以上
    if snd5s != "＜推定５弱以上＞":

        length = 0
        for i in snd5s:
            length+=1
        #判定情報字數
        row = length//36+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = snd5s[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            print("5-以上")
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid3 != logid2:
                exit()

    #震度4
    if snd4 != "＜震度４＞":

        length = 0
        for i in snd4:
            length+=1
        #判定情報字數
        row = length//36+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = snd4[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            print("4")
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid3 != logid2:
                exit()

    #震度3
    if snd3 != "＜震度３＞":

        length = 0
        for i in snd3:
            length+=1
        #判定情報字數
        row = length//36+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = snd3[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            print("3")
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid3 != logid2:
                exit()

    #震度2
    if snd2 != "＜震度２＞":

        length = 0
        for i in snd2:
            length+=1
        #判定情報字數
        row = length//36+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = snd2[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            print("2")
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid3 != logid2:
                exit()

    #震度1
    if snd1 != "＜震度１＞":

        length = 0
        for i in snd1:
            length+=1
        #判定情報字數
        row = (length//36)+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = snd1[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            print("1")
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid3 != logid2:
                exit()


f = open("output.txt", "w",encoding="utf8")
f.write("")
f.close()
#清空輸出資料
exit()