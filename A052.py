N = int(input())
A,B = list(map(int,input().split()))
def saishoukoubaisuu(a,b):
    sosuu = [2,3,5,7]
    plassnum = 1
    c = True
    while(c):
        c = False
        for num in sosuu:
            if a%num==0 and b%num==0:
                a=a//num
                b=b//num
                plassnum*=num
                c = True
    return(a*b*plassnum)
len = saishoukoubaisuu(A,B)
kaidan = [True for _ in range(len)]

for i in range(0,len,A):
    # print(i,"i")
    for j in range(0,len-i,B):
        print(j,"j")
        if i==0 and j ==0:
            continue
        print(i+j-1,"i+j-1")
        kaidan[i+j-1]=False
# print(kaidan)
count_len = kaidan.count(True)
m = (N//len)
ans = m*count_len+kaidan[:N-len*m].count(True)
if N%A!=0 and N%B!=0:
    ans+=1
print(kaidan[:N-len*m])
print(ans)