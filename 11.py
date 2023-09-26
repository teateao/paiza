n=int(input())
d=[int(input()) for x in range(n)]
a=0
d.sort()
for i in d:
    if i==a:
        d.remove(i)
    a=i