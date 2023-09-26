N,X,Y = map(int,input().split())
print(N)
for i in range(N):
    A=""
    if(i%X):
        A+="A"
    elif(i%Y):
        A+="B"
        print(A)
    else:
        print("N")