n = int(input())
warks = [list(map(int,input().split())) for (x) in range(n)]

a=0
for i in warks:
    for j in i:
        if j > a :
            a=j

calendar = list(False for _ in range(a))

for wark in warks:
    count=wark[0]-1
    while count!=wark[1]:
        calendar[count]=True
        count+=1

count=0
b=0
for i in calendar:
    if i:
        count+=1
    else:
        if b < count:
            b=count
        count=0
if b < count:
    b=count

print(b)