# -*- coding: utf-8 -*-
from asyncore import write
import time
import requests
import urllib3
from area import *
from eqstation import *
urllib3.disable_warnings()

url = "https://api.p2pquake.net/v2/history?codes=551"

def num(y):
    y = y.replace("1","１").replace("2","２").replace("3","３").replace("4","４").replace("5","５").replace("6","６").replace("7","７").replace("8","８").replace("9","９").replace("0","０")
    return y

def replaceint(x):
    x = x.replace("県","").replace("府","").replace("東京都","東京").replace("新島","新島地方").replace("鹿児島","").replace("地方","").replace("檜山","檜山地方").replace("北海道","").replace("網走","網走地方").replace("北見","北見地方").replace("紋別","紋別地方").replace("青森津軽","津軽").replace("庄内","庄内地方").replace("最上","最上地方").replace("村山","村山地方").replace("置賜","置賜地方").replace("福島会津","会津").replace("埼玉秩父","秩父地方").replace("新潟上越","新潟上越地方").replace("新潟中越","新潟中越地方").replace("新潟下越","新潟下越地方").replace("新潟佐渡","佐渡地方").replace("石川能登","能登地方").replace("石川加賀","加賀地方").replace("福井嶺北","福井嶺北地方").replace("福井嶺南","福井嶺南地方").replace("岐阜飛騨","飛騨地方").replace("静岡地方","伊豆地方").replace("兵庫淡路島","淡路島").replace("奈良","奈良県").replace("島根隠岐","隠岐").replace("予","予地方").replace("福岡福岡","福岡地方").replace("福岡北九州","北九州地方").replace("福岡筑豊","筑豊地方").replace("福岡筑後","筑後地方").replace("長崎島原半島","島原半島").replace("長崎対馬","対馬").replace("長崎壱岐","壱岐").replace("長崎五島","五島").replace("熊本阿蘇","阿蘇地方").replace("熊本熊本","熊本地方").replace("熊本球磨","球磨地方").replace("熊本天草・芦北","天草・芦北").replace("薩摩","薩摩地方").replace("大隅","大隅地方").replace("沖縄","").replace("本島","沖縄本島") 
    return x

def log():
    logfile = open('P2PV2log.txt', encoding="utf8")
    log3 = logfile.read()
    logfile.close()
    if log3 != log2:
        exit()
    pass

def file(z="",y=5):
    print(z)
    f = open("P2PV2output.txt", "w",encoding="utf8")
    f.write(z)
    f.close()
    time.sleep(y)

data = requests.get(url, verify=False).json() #取得資料

log2 = data[0]["id"] #情報ID

logfile = open("P2PV2log.txt", encoding="utf8")
log1 = logfile.read()
logfile.close

if log1 == log2:
    exit()

f = open("P2PV2log.txt", "w",encoding="utf8")
f.write(log2)
f.close()

earthquake = data[0]["earthquake"] #震源情報
tsunami = earthquake["domesticTsunami"] #日本國內海嘯情報/国内津波情報
foreigntsunami = earthquake["foreignTsunami"] #海外海嘯情報/海外津波情報
loc = earthquake["hypocenter"]["name"] #震央地名
dep = earthquake["hypocenter"]["depth"] #深度/深さ
mag = earthquake["hypocenter"]["magnitude"] #規模
maxint = earthquake["maxScale"] #最大震度
eventtime = earthquake["time"] #地震發生時間/地震発生時刻

datatype = data[0]["issue"]["type"] #情報種類

points = data[0]["points"] #震度観測点

int_dic = {70:"震度７", #震度dic
60:"震度６強",
55:"震度６弱",
50:"震度５強",
45:"震度５弱",
46:"推定５弱",
40:"震度４",
30:"震度３",
20:"震度２",
10:"震度１"}

datatype_dic = {"ScalePrompt":"震度速報", #情報種類
"Destination":"震源速報",
"ScaleAndDestination":"震源震度",
"DetailScale":"各地震度",
"Foreign":"遠地地震",
"Other":"その他"}

tsunami_dic = {"None":"この地震による津波の心配はありません", #日本國內的海嘯情報/国内の津波情報
"Unknown":"日本への津波の有無については不明です",
"Checking":"日本への津波の有無については現在調査中です",
"NonEffective":"日本の沿岸で多少の潮位変動があるかもしれませんが　被害の心配はありません",
"Watch":"津波注意報を発表中です",
"Warning":"津波警報等を発表中です"}

foreigntsunami_dic = {"NonEffectiveNearby":"震源の近傍で小さな津波発生の可能性がありますが　被害の心配はありません", #日本國外的海嘯情報/海外の津波情報
"WarningNearby":"震源の近傍で津波発生の可能性があります",
"WarningPacific":"太平洋で津波発生の可能性があります",
"WarningPacificWide":"太平洋の広域に津波発生の可能性があります",
"WarningIndian":"インド洋で津波発生の可能性があります",
"WarningIndianWide":"インド洋の広域で津波発生の可能性があります",
"Potential":"一般にこの規模では津波発生の可能性があります"}

for i in datatype_dic:
    if i == datatype:
        datatype = datatype_dic[i]

hou = int(eventtime[11:13])
min = eventtime[14:16]
if hou > 11:
    hou -= 12
    ampm = "午後"
else:
    ampm = "午前"
hou = str(hou)

if min[:1] == "0":
    min = min.replace("0","",1)    

eventtime = f"{ampm}{hou}時{min}分頃"

eventtime = num(eventtime)

if datatype == "震源速報":
    for i in range(10):
        if data[i]["issue"]["type"] == "ScalePrompt":
            points = data[i]["points"]
            break

eq_dic = {}
for i in points:
    if datatype != "震度速報" and datatype != "震源速報":
        for j in eqstation:
            if i["addr"] == j:
                if eqstation[j] in eq_dic:
                    pass
                else:
                    eq_dic[eqstation[j]] = i["scale"]
    else:
        eq_dic[replaceint(i["addr"])] = i["scale"]


a = 0
area = ""
lastarea = ""
if datatype == "震度速報":
    for y in eq_dic.items():
        if y[1] == maxint:
            for i in 地域:
                for j in i['list']:
                    if y[0] == replaceint(j):
                        if lastarea != i['name']:
                            area += '・' + i['name']
                            lastarea = i['name']
    area = area[1:]
    area = f"　{area}地方で"

strength = ""
if datatype == "震度速報":
    if maxint == 70 or maxint == 60 or maxint == 55 or maxint == 50 or maxint == 45:
        strength = "強い"
    elif maxint == 40:
        strength = "やや強い"

far = ""
if datatype == "遠地地震":
    far = "　海外で規模の大きな"

a = 0
for i in loc:
    a += 1

dep = str(dep)
mag = str(mag)

if dep == "-1":
    dep = "不明"
elif dep == "0":
    dep = "ごく浅い"
else:
    dep += "キロ"
if mag == "-1":
    mag = "不明"
mag = mag.replace(".",". ")

tsunamiinfo = []
try:
    tsunamiinfo.append(tsunami_dic[tsunami])
except:
    pass
try:
    tsunamiinfo.append(foreigntsunami_dic[foreigntsunami])
except:
    pass

if len(eq_dic) >= 50 and len(eq_dic) < 100:
    g = 4
elif len(eq_dic) >= 100 and len(eq_dic) < 200:
    g = 3
elif len(eq_dic) >= 200:
    g = 2
else:
    g = 5
if datatype == "震度速報":
    g = 20

file("地震情報",2)
for i in range(g):
    file(f"{eventtime}{area}{far}{strength}地震がありました")
    log()

    if datatype != "震度速報":
        if a < 18:
            file(num(f"震源は{loc}　深さ{dep}　マグニッチュード{mag}"))
            log()
        else:
            file(num(f"震源は{loc}"))
            log()
            file(num(f"深さ{dep}　マグニッチュード{mag}"))
            log()

        for i in tsunamiinfo:
            file(i)
            log()

    for j in int_dic:
        output = ""
        nextoutput = ""
        for i in eq_dic.items():
            if i[1] == j:
                nextoutput = output + "　" + i[0]
                output_len = 0
                for w in nextoutput:
                    output_len += 1
                if output_len > 31:
                    file(int_dic[j] + output)
                    log()
                    output = ""
                output += "　" + i[0]
        if output == "":
            continue
        file(int_dic[j] + output)
        log()
file("",0)