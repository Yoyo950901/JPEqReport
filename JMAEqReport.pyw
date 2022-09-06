# -*- coding: utf-8 -*-
from asyncore import write
from calendar import month
from dis import code_info
from encodings import utf_8
import time
import requests
import urllib3
import xmltodict
import os
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
urllib3.disable_warnings()

xml = requests.get("https://www.data.jma.go.jp/developer/xml/feed/eqvol.xml")
xml = requests.get("https://www.data.jma.go.jp/developer/xml/feed/eqvol_l.xml") #測試用 最新1周資料
xml.encoding = "utf-8"
#取得気象庁XML(地震/火山相關)

sp = BeautifulSoup(xml.text, 'xml')

if xml.status_code == 200:
    print("資料取得正常")
else:
    print("資料取得失敗，請檢查網路或氣象廳網站是否正常")
    exit()
#判定資料是否取得正常


logfile = open("JMAlog.txt", encoding="utf8")
logid1 = logfile.read()
logfile.close
#讀取上次情報ID

print(sp.title.text)
z = ""
for i in sp.select("entry"): #搜尋地震相關的XML
    if "VXSE51" in i.id.text or "VXSE52" in i.id.text or "VXSE53" in i.id.text or "VXSE61" in i.id.text:
        url = i.id.text
        z = "a"
        break

if z == "":
    print("未取得地震資訊")
    exit()

def log():
    logfile = open('JMAlog.txt', encoding="utf8")
    log3 = logfile.read()
    logfile.close
    if log3 != log2:
        exit()

def file(y=5):
    print(output)
    f = open("JMAoutput.txt", "w",encoding="utf8")
    f.write(output)
    f.close()
    time.sleep(y)

url = "http://www.yoyo0901.byethost16.com/%e5%9c%b0%e9%9c%87%e6%83%85%e5%a0%b1/%e9%9c%87%e6%ba%90%e3%83%bb%e9%9c%87%e5%ba%a6%e3%81%ab%e9%96%a2%e3%81%99%e3%82%8b%e6%83%85%e5%a0%b1%20VXSE53/32-39_11_05_120615_VXSE53.xml" #test

#xml2 = requests.get(url) #取得資料

headers1 = dict() #test
headers1["Cookie"]="__test=eb3f55df3488e2eb5ad76e961a3d8e90; _test=6c0c461aa22234658c3ed583b610179e" #test

xml2 = requests.get(url,headers=headers1) #test

xml2.encoding = "utf-8"
xml2=xmltodict.parse(xml2.text) #XML轉JSON

data = xml2["Report"] #資料主體

title = data["Head"]["Title"] #標題
headline = data["Head"]["Headline"]["Text"] #註解文
earthquake = data["Body"]["Earthquake"] #地震資訊

eventtime = data["Head"]["EventID"] #地震發生時間
mon = eventtime[4:6]
day = eventtime[6:8]
hou = int(eventtime[8:10])
min = eventtime[10:12]
if hou > 11:
    hou -= 12
    ampm = "午後"
else:
    ampm = "午前"
hou = str(hou)

a = [mon,day,hou,min]

if mon[:1] == "0":
    mon = mon.replace("0","")
if day[:1] == "0":
    day = day.replace("0","")
if hou[:1] == "0":
    hou = hou.replace("0","")
if min[:1] == "0":
    min = min.replace("0","")    

if "震源要素更新" in title:
    eventtime = f"{mon}月{day}日{ampm}{hou}時{min}分頃"
else:
    eventtime = f"{ampm}{hou}時{min}分頃"



try:
    intensity = data["Body"]["Intensity"]["Observation"] #震度資訊
    pref = intensity["Pref"]
    maxint = intensity["MaxInt"]
except:
    intensity = ""
    pref = ""
    maxint = ""
    print("未取得震度資訊")

a = 0
b = 0
c = 0
cityint = {}
areaint = {}

for i in pref:
    if type(i) == str:
        i = pref
        a = 1
    for j in i["Area"]:
        if type(j) == str:
            j = i["Area"]
            b = 1
        try:
            for k in j["City"]:
                if type(k) == str:
                    k = j["City"]
                    c = 1
                cityint[k["Name"]] = k["MaxInt"]

                if c == 1:
                    break
        except:
            pass

        areaint[j["Name"]] = j["MaxInt"]
        
        if b == 1:
            break
    if a == 1:
        break

print(eventtime)