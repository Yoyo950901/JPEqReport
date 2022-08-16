# -*- coding: utf-8 -*-
from asyncore import write
import time
import requests
import urllib3
import os
'''
import random
n=random.randrange(0,100)
'''
urllib3.disable_warnings()
#print(n)
url = "https://api.p2pquake.net/v1/human-readable?limit=100"

data = requests.get(url, verify=False).json()[49]

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
#print(data)
print(震度)
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
                    print(震度列表[y]+output[0:-1])
                    output=''
                else:
                    output=output + 震度[a]["addr"] + "　"
            a=a+1
        output = 震度列表[y]+output[0:-1]
        print(output)
        time.sleep(10)

for j in range(0,10):
    scale(j)
