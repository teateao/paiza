N, H, W = list(map(int, (input().split())))
# maping = [[0 for j in range(W)] for i in range(H)]
citys = []
for i in range(N):
    x, y = list(map(int, (input().split())))
    # maping[y-1][x-1] = 1
    citys.append({"id": i, "x": x, "y": y, "way": []})
for i in range(len(citys)):
    x = citys[i]("x")
    y = citys[i]("y")
    for city in citys:
        way = min(abs(x-city("x")), abs(x-(city("x")-H)),) + \
            min(abs(y-city("y")),abs((y-W)-city("y")))
        citys[i]("way").append(way)
ans = []
id = 0
for i in range(len(citys)-1):
    anser = 0
    for j in range(len(citys)-i):
        anser+=citys[i+j]("way")[j]
