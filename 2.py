N,M=map(int,input().split())
n_gondora=[int(input()) for (x) in range(N)]
m_ninzuu=[int(input()) for (x) in range(M)]
kaitou=[0 for (x) in range(N)]
# for i in range(N):
#     n_gondora.append(int(input()))
#     kaitou.append(0)
# for i in range(M):
#     m_ninzuu.append(int(input()))
count=1
while (len(m_ninzuu)>0):
    i=n_gondora[count-1]
    j=m_ninzuu[0]
    
    if i>=j:
        kaitou[count-1]+=j
        del m_ninzuu[0]
    else:
        kaitou[count-1]+=i
        m_ninzuu[0]-=i
    if count<N:
        count+=1
    else:
        count=1
for i in kaitou:
    print(i)
