N,M,K=map(int,input().split())

n=[]
for i in range(1,N+1):
    n.append(i)


def divide(a):
    b=[]
    b1=[]
    count=0
    for i in a:
        b1.append(i)
        count+=1
        if count%M==0:
            b.append(b1)
            b1=[]
    if len(b1)>0:
        b.append(b1)
    return b


def shuffle(b):
    c=[]
    while len(b)!=0:
        c.append(b[len(b)-1])
        b.pop()
    d=[]
    for i in c:
        for j in i:
            d.append(j)
    return d

for i in range(K):
    a=divide(n)
    n=shuffle(a)

for i in n:
    print(i)