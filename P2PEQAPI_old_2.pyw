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
深さ = eq["hypocenter"]["depth"]
規模 = eq["hypocenter"]["magnitude"]
震源地= eq["hypocenter"]["name"]
最大震度 = eq["maxScale"]
発生日時 = eq["time"]
情報種類 = data["issue"]["type"]
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
    津波情報 = "この地震で若干の海面の変動あり　津波の被害の心配はありません"
elif 津波情報 == "Watch":
    津波情報 = "この地震で津波注意報発表中"
elif 津波情報 == "Warning":
    津波情報 = "この地震で津波警報等発表中　直ちに高台に避難してください"
#判定海嘯情報種類

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

if 情報種類 == ("DetailScale"):
    #地震情報(各地の震度)
    print("地震情報")

    for i in range(10):

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

    for i in range(10):

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
    
    for i in range(10):

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

    for i in range(15):

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

elif 情報種類 == ("Foreign"):
    #遠地地震
    print("遠地地震")

    for i in range(10):

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


f = open("output.txt", "w",encoding="utf8")
f.write("")
f.close()
#清空輸出資料
exit()