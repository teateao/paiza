H,W = map(int,input().split())
boards =[list(map(int,input().split())) for _ in range(H)]
anser = []
for i in boards[0]:
    anser.append([i])
count1 = 0 #行
while(H-1!=count1):
    count1+=1
    count2 = 0 #左から何番目
    new_anser=[[] for _ in range(W)]
    while(W!=count2):
        if count2!=0:
            for i in anser[count2-1]:
                new_anser[count2].append(i+boards[count1][count2])
        for i in anser[count2]:
            new_anser[count2].append(i+boards[count1][count2])
        if count2!=W-1:
            for i in anser[count2+1]:
                new_anser[count2].append(i+boards[count1][count2])
        count2 += 1
    a = []
    for i in new_anser:
        a.append([max(i)])
    anser = a
a=[]
for i in anser:
    a.append(max(i))
print(max(a))