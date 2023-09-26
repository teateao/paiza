h, w = list(map(int, input().split()))
l = ["."]*(w+2)
mapping = [list("."+input()+".") for i in range(h)]
mapping.insert(0, l)
mapping.append(l)
# for i in mapping:
#     print(i)
islands = []
for the_h in range(1, h+1):
    for the_w in range(1, w+1):
        if mapping[the_h][the_w] == "#":
            menseki = 1
            hyoumennseki = 0
            zahyou = [[the_h, the_w]]
            for i in list(set(zahyou)):
                mapping[i[0]][i[1]] = "-"
                # print("i",end=":")
                # print(i)
                if mapping[i[0]+1][i[1]] == "#":
                    zahyou.append([i[0]+1, i[1]])
                    mapping[i[0]+1][i[1]] = "-"
                    menseki += 1
                elif mapping[i[0]+1][i[1]] == ".":
                    hyoumennseki += 1
                if mapping[i[0]-1][i[1]] == "#":
                    zahyou.append([i[0]+1, i[1]])
                    mapping[i[0]-1][i[1]] = "-"
                    menseki += 1
                elif mapping[i[0]-1][i[1]] == ".":
                    hyoumennseki += 1
                if mapping[i[0]][i[1]+1] == "#":
                    zahyou.append([i[0], i[1]+1])
                    mapping[i[0]][i[1]+1] = "-"
                    menseki += 1
                elif mapping[i[0]][i[1]+1] == ".":
                    hyoumennseki += 1
                if mapping[i[0]][i[1]-1] == "#":
                    zahyou.append([i[0], i[1]-1])
                    mapping[i[0]][i[1]-1] = "-"
                    menseki += 1
                elif mapping[i[0]][i[1]-1] == ".":
                    hyoumennseki += 1
                # print("i",end=":")
                # print(i)
                # print("menseki",end=":")
                # print(menseki)
                # print("hyoumennseki",end=":")
                # print(hyoumennseki)
                # for i in mapping:
                    # print(i)
                
            islands.append([menseki, hyoumennseki])


def anssort(list):
    a = list[0]
    b = list[1]
    return -(a*1000+b)


anser = sorted(islands, key=anssort)
for i in anser:
    print(*i, sep=',')
