N = int(input())
gameBoard = [list(map(int,list(input()))) for _ in range(N)]
anser = []
arounds = [[-1, -1], [-1, 0], [-1, 1],[0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
for i in range(N):
    for j in range(N):
        # print("今の座標"+str(i),str(j))
        for around in arounds:
            ansercount = 0
            before = gameBoard[i][j]
            count = 0
            plus = True
            minus = True
            while plus or minus:
                count += 1
                ansercount += 1
                if 0 <= i+around[0]*count < N and 0 <= j+around[1]*count < N:
                    # print("next"+str(i+around[0]*count),str(j+around[1]*count))
                    # print(ansercount)
                    next = gameBoard[i+around[0]*count][j+around[1]*count]
                    if before-next != 1:
                        plus = False
                    if before-next != -1:
                        minus = False
                    before = next
                else:
                    # ansercount+=1
                    break
            anser.append(ansercount)
print(max(anser))