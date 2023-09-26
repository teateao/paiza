n= int(input())
calender = list(map(int,input().split()))

tokuteino_isshuukan=[]
count = 0
anser = 0
for i in range(len(calender)-6):
    tokuteino_isshuukan = [calender[i+j] for j in range(7)]
    # [i,i+1,i+2,i+3...]
    if sum(tokuteino_isshuukan) > 5:
        if anser < count:
            anser = count
        count=0
    else:
        count+=1
    # print(tokuteino_isshuukan)
if anser < count:
    anser = count

if anser!=0:
    anser+=6

print(anser)