N, X, F, S = map(int, input().split())
# Nが全体　Xが最大効率 Fが１時間で下がる効率　Sが１時間で上がる効率
# [time,今の効率,進捗]
all = [[1, max([0, X-F]), X]]
anser = 2000
newall = []
while (True):
    for i in all:
        # 寝る
        if i[1] != X and i[0] < anser:
            newall.append([i[0]+3, min([i[1]+S*3, X]), i[2]])
        # 寝ない
        if i[1] != 0 and i[0] < anser:
            if i[2]+i[1] <= N:
                newall.append([i[0]+1, max([0, i[1]-F]), i[2]+i[1]])
            else:
                anser = min([anser, i[0]+1])
    if len(newall)==0:
        break
    all = newall
    print(all)
    newall.clear
print(anser)