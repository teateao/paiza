n,m=map(int,input().split())
kaito_hz=[]
for i in range(m):
    kaito_hz.append(int(input()))
hz=[]
zenin_hz=[]
for i in range(n):
    for j in range(m):
        hz.append(int(input()))
    zenin_hz.append(hz)
    hz=[]
saikoutokuten=0
for i in zenin_hz:
    tensu=100
    count=0
    while m!=count:
        zure=abs(i[count]-kaito_hz[count])
        if zure<=5 or tensu==0:
            tensu-=0
        elif zure<=10 and tensu>=1:
            tensu-=1
        elif zure<=20 and tensu>=2:
            tensu-=2
        elif zure<=30 and tensu>=3:
            tensu-=3
        elif tensu>=5:
            tensu-=5
        else:
            tensu=0
        count+=1
    if saikoutokuten<tensu:
        saikoutokuten=tensu
print(saikoutokuten)
