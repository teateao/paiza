n = int(input())
m=[]
for i in range(n):
    a=int(input())
    m.append(a)

count=1
count2=0

while len(m) != 0:
    l=[]
    for i in m:
        if count== i:
            count+=1
        else:
            l.append(i)
        if n==i:
            count2+=1
    m=l
print(count2-1)
