N,M,G = map(int,input().split())
window = [input().split() for _ in range(M)]
Groops=[str(G)]
isroop = True
road = []
def has_duplicates(seq):
    a = set(seq)
    if len(seq) != len(a):
        for i in a:
            seq.pop(i)
        return([True,seq])
    else:
        return([False,[]])
while(isroop):
    isroop = False
    for i in window:
        newGroops=[]
        for Groop in Groops:
            if i[0]==Groop:
                newGroops.append([Groop+i[1]])
                isroop = True
        Groops = newGroops
# while(isroop):
#     isroop = False
#     for i in window:
#         for Groop in Groops:
#             if i[0]==Groop:
#                 Groop=i[1]
#                 roop.append(Groop)
#                 isroop = True
#     if Groop==G:
#         break

# nokoris = [j+1 for j in range(N)]
# for i in roop:
#     nokoris.pop(i)

# for i in window:
#     i
# while(isroop):
#     for nokori in nokoris:
#         isroop = False