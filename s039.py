H, W = map(int, input().split())
labyrinth = []
kabe = "#" * (W+2)
labyrinth.append(kabe)
for _ in range(H):
    labyrinth.append("#"+input()+"#")
labyrinth.append(kabe)

anser = []
count_H = 0
while (count_H < H):
    count_H += 1
    count_W = 0
    while (count_W < W):
        count_W += 1
        if labyrinth[count_H][count_W] == ".":  # 初期値の座標
            h = count_H  # 元の変数を変えないための代用
            w = count_W
            # ここからできるだけ縦に伸ばしていく
            count_h = 0
            while (True):
                h += 1
                count_h += 1
                if labyrinth[h][w] == "#":
                    break
            print(str(count_H)+","+str(count_W))
            print(str(count_h)+"*"+"1="+str(count_h))
            anser.append(count_h)
            h = count_H
            # ここから縦に伸ばしたマス目から横に伸ばせるか
            horizontal = 1  # よこ
            a = count_h  # aは前回のたてここではできるだけ縦に伸ばしたcount_hを初期値している
            while (True):
                if labyrinth[h][w+1] == "#":  # 横に伸ばせるか判定
                    break
                else:  # ここから横に伸ばせ得るときの処理
                    w += 1
                    vertical = 1  # たて
                    horizontal += 1
                    print("aは"+str(a))
                    for i in range(a):  # 一つ左のたては越えれない
                        print(h,w)
                        if labyrinth[h+i+1][w] == ".":
                            vertical += 1
                        else:
                            print(str(count_H)+","+str(count_W))
                            print(str(vertical)+ "*"+str(horizontal)+"="+str(horizontal*vertical))
                            anser.append(horizontal*vertical)
                            break
                    a = vertical
print(anser)
