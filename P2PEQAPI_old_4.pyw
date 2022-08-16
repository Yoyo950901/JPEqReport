# -*- coding: utf-8 -*-
from asyncore import write
import time
import requests
import urllib3
import os
urllib3.disable_warnings()

url = "https://api.p2pquake.net/v1/human-readable?limit=10"

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

if 深さ == "-1km":
    深さ = "不明"


震度代碼= [70,60,55,50,45,46,40,30,20,10]
震度列表= ["震度７　","震度６強　","震度６弱　","震度５強　","震度５弱　","推定５弱　","震度４　","震度３　","震度２　","震度１　"]

    
def scale(y):
#各地震度函數
    a=0
    output = ""
    for i in 震度:
        if (震度[a]["scale"]) == 震度代碼[y]:
            output = output + 震度[a]["addr"] + "　"
        a=a+1
    #獲取完全資料以供下面分辨

    if 震度列表[y] + output[0:-1] != 震度列表[y]:
    #分辨震度是否有資料，若無跳過
    

        output=''
    #初始化正式迴圈
        a=0
        for i in 震度:
            if (震度[a]["scale"]) == 震度代碼[y]:
            #分離所需震度

                本次輸出 = output + 震度[a]["addr"] + "　"

                字數=0
                for b in 本次輸出:
                    字數=字數+1
                #本次迴圈字數


                if 字數 > 31:
                    output = (震度列表[y]+output[0:-1])
                    f = open("output.txt", "w",encoding="utf8")
                    f.write(output)
                    f.close()
                    time.sleep(8)

                    logfile = open('log.txt', encoding="utf8")
                    logid3 = logfile.read()
                    logfile.close
                    if logid2 != logid3:
                        exit()
                    output=''

                output=output + 震度[a]["addr"] + "　"
            a=a+1
        output = 震度列表[y]+output[0:-1]
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(8)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()



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
        time.sleep(8)

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
        time.sleep(8)

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
        time.sleep(8)

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
        time.sleep(8)

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
        time.sleep(8)

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
        time.sleep(8)

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
        time.sleep(8)

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
        time.sleep(8)

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
        time.sleep(8)

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
        time.sleep(8)

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
        time.sleep(8)
        
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
        time.sleep(8)

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
        time.sleep(8)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()


    for j in range(0,10):
        scale(j)


f = open("output.txt", "w",encoding="utf8")
f.write("")
f.close()
#清空輸出資料
exit()