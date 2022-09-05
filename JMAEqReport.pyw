# -*- coding: utf-8 -*-
from asyncore import write
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

xml2 = requests.get(url) #取得資料

xml2.encoding = "utf-8"
xml2=xmltodict.parse(xml2.text) #XML轉JSON

data = xml2["Report"] #資料主體
title = data["Head"]["Title"] #標題
headline = data["Head"]["Headline"]["Text"] #註解文