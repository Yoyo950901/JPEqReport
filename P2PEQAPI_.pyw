# -*- coding: utf-8 -*-
from tkinter import E
import requests
import urllib3
urllib3.disable_warnings()

api鏈接 = "https://api.p2pquake.net/v1/human-readable?limit=1"

數據 = requests.get(api鏈接, verify=False).json()[0]



地震='earthquake'

深度='depth'

規模='magnitude'

位置='name'

最大震度='maxScale'

建立時間='created_at'

地震時間='time'

各地震度='point'


print(數據)
print("\n")
print(數據['created_at'])
print("\n")
print(數據[地震])


length = 0

for i in 數據[各地震度]:
    print(數據[各地震度][length])
    length+=1