n = list(map(int, input().split()))
labyrinth = []
for _ in range(n[1]):
    l = list(input().split())
    labyrinth.append(l)

answer = 0
a=True
tesu = [[0,1],[0,-1],[1,0],[-1,0]]
while a:
    x=1
    new_labyrinth=[]
    b=True
    while x <= n[1]:
        y=1
        while y <= n[0]:
            if labyrinth[x][y] == "s":
                for c,d in tesu:
                    kansen = labyrinth[x+c][y+d]
                    if kansen == "1" or kansen=="s":
                        continue
                    elif kansen == "0":
                        new_labyrinth.append([x+c,y+d])
                    elif kansen == "g":
                        a=False
                    b=False
            y+=1
        x+=1
    if b:
        a=False
    for i in new_labyrinth:
        labyrinth[i[0]][i[1]] = "s"
    answer+=1

if b:
    print("Fail")
else:
    print(answer)