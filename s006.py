import math
a,b,x,y,r,theta,L = list(map(int,input().split()))
# a,b　縦横
# x y 最初の球の座標
# r　球の半径
# l 打ち出す角度
# L 転がる距離
A = a-r*2
B = b-r*2
# print("A,B",end=":")
# print(A,B)
# そのまま進む時の座標
X = L*math.cos(math.radians(theta))+x
Y = L*math.sin(math.radians(theta))+y
print("X,Y",end=":")
print(X,Y)
# 計算結果
result_x = [X//A,X%A]
result_y = [Y//B,Y%B]
print("result",end=":")
print(result_x,result_y)
# アンサー
anser_x = result_x[1]
anser_y = result_y[1]
if result_x[0]%2==0:
    anser_x = A-anser_x
if result_y[0]%2==0:
    anser_y = A-anser_y
anser_x+=r
anser_y+=r
print(anser_x,anser_y)