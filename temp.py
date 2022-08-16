import math
import time
b=''
for i in range(12):
    for i in range(1,10):
        c=str(i)
        b=str(b)+c*10

b=b[0:1000]
#print(b)
#b='b'*1000
s=0
for i in b:
    s=s+1
#print(s)
n=math.ceil(s/32)
#print(n)
a=0
q=0
for i in range(0,n):
    q=n*i
    x=q+32
    print(b[q:x])
    q=q+1
    time.sleep(1)