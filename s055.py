H, W = map(int, input().split())
zoo = [input().split() for _ in range(H)]
n = int(input())
food_chain_list = [input().split() for _ in range(n)]
zoo_list = [] 

# 動物の種類を求める
for food_chain in food_chain_list:
    animal_bool_0 = True
    animal_bool_1 = True
    for animal in zoo_list:
        if food_chain[0] == animal:
            animal_bool_0 = False
        if food_chain[1] == animal:
            animal_bool_1 = False
    if animal_bool_0:
        zoo_list += food_chain[0]
    if animal_bool_1:
        zoo_list += food_chain[1]
zoo_list = sorted(zoo_list)
# 処理を開始する（頂点に立つものを求める)
def top_animal():
    for animal in zoo_list:
        top_bool = True  # トップになる可能性
        for food_chain in food_chain_list:
            if food_chain[1] == animal:
                top_bool = False
        if top_bool:
            return (animal)

# ここから捕食者ポジション
def predation(top):
    count2 = 0
    top_animal_list = []
    for i in zoo:
        count1 = 0
        for j in i:
            if j == top:
                top_animal_list.append([count2, count1])
            count1 += 1
        count2 += 1
    return(top_animal_list)

# ここから被食者ポジション
def preys(top):
    for _ in range(len(zoo_list)):
        top_list = predation(top)
        preys = []
        for top_position in top_list:
            preys.append([top_position[0]+1,top_position[1]-1])
            preys.append([top_position[0]+1,top_position[1]])
            preys.append([top_position[0]+1,top_position[1]+1])
            preys.append([top_position[0]-1,top_position[1]-1])
            preys.append([top_position[0]-1,top_position[1]])
            preys.append([top_position[0]-1,top_position[1]+1])
            preys.append([top_position[0],top_position[1]+1])
            preys.append([top_position[0],top_position[1]-1])
    return(preys)
# 被食者の名前
def prey_list(top):
    list = []
    count=0
    countlist = []
    for food_chain in food_chain_list:
        if food_chain[0] == top:
            list.append(food_chain[1])
            countlist.append(count)
        count+=1
    for _ in range(len(countlist)):
        food_chain_list.pop(countlist.pop())
    return(list)

# 消す
for _ in range(len(zoo_list)):
    top = top_animal() #加害者
    if top == None:
        break
    preylist = prey_list(top) #被害者になり得る動物
    preys_positions = preys(top) #被害者になり得る場所
    disappears = [] #消すリスト
    count1=0
    for zooline in zoo:
        count2 = 0
        for animal in zooline:
            for prey in preylist:
                if animal == prey:
                    for preys_position in preys_positions:
                        if count1 == preys_position[0] and count2 == preys_position[1]:
                            disappears.append([count2,count1])
            count2+=1
        count1+=1
    for disappear in disappears:
        zoo[disappear[1]][disappear[0]] = "-"
    if len(zoo_list)!=0:
        zoo_list.remove(top)
for i in zoo:
    line=""
    for j in i:
        line+= j +" "
    print(line[:-1])
