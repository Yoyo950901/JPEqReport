# -*- coding: utf-8 -*-
from asyncore import write
import time
import requests
import urllib3
import os
urllib3.disable_warnings()

api鏈接 = "https://api.p2pquake.net/v1/human-readable?limit=1"

數據 = requests.get(api鏈接, verify=False).json()[0]

if 數據["code"] != (551):
    exit()

logfile = open('log.txt', encoding="utf8")
logid1 = logfile.read()
logfile.close
logid2 = 數據["_id"]["$oid"]

if logid1 == logid2:
    exit()
        
地震='earthquake'

深度='depth'

規模='magnitude'

位置='name'

最大震度=數據[地震]["maxScale"]

建立時間='created_at'

地震時間=數據[地震]['time']

各地震度='point'

海嘯=數據[地震]['domesticTsunami']

if 最大震度 == 10:
    最大震度 = ("1")
elif 最大震度 == 20:
    最大震度 = ("2")
elif 最大震度 == 30:
    最大震度 = ("3")
elif 最大震度 == 40:
    最大震度 = ("4")
elif 最大震度 == 45:
    最大震度 = ("5弱")
elif 最大震度 == 50:
    最大震度 = ("5強")
elif 最大震度 == 55:
    最大震度 = ("6弱")
elif 最大震度 == 60:
    最大震度 = ("6強")
elif 最大震度 == 70:
    最大震度 = ("7")

if 海嘯 == "None":
    海嘯 = "この地震による津波の心配はありません。"
elif 海嘯 == "Unknown":
    海嘯 = "津波情報不明。"
elif 海嘯 == "Checking":
    海嘯 = "津波有無調查中。"
elif 海嘯 == "NonEffective":
    海嘯 = "この地震で、多少の潮位の変化ある、津波の被害の心配はありません。"
elif 海嘯 == "Watch":
    海嘯 = "この地震で、津波注意報が発表されました。"
elif 海嘯 == "Warning":
    海嘯 = "この地震で、津波警報が発表されました、直ちに高台に避難してください。"



output = ("　"*20+"【地震情報】"+地震時間+"頃地震がありました、震源地は"+數據[地震]['hypocenter'][位置]+"、深さは約"+數據[地震]['hypocenter'][深度]+"、規模はM"+數據[地震]['hypocenter'][規模]+"、最大震度"+最大震度+"。"+海嘯+"　"*25)


f = open("log.txt", "w",encoding="utf8")
f.write(數據["_id"]["$oid"])
f.close()

f = open("output.txt", "w",encoding="utf8")
f.write(output)
f.close()

time.sleep(300)


f = open("output.txt", "w",encoding="utf8")
f.write("")
f.close()
exit()