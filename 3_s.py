k, s, t = map(int, input().split())
count = 0
s_mae = ""
s_t = ""
t_usiro = ""
while (k > 10):
    a = 3
    for _ in range(k-2):
        a = 2*a + 3
    if 1 == s:
        s_mae += "A"
        s += 1
    if 1 == t:
        s_mae = s_mae[:-1]
        t+=1
    if a+2 == s:
        s_mae += "B"
        s += 1
    if a+2 == t:
        t_usiro += "B"
        t-=1
    if a*2+3 == s:
        s_mae += "C"
        s -=1
    if t == a*2+3:
        t_usiro += "C"
        t -= 1
    if t <= a+2 and s < a+2:  # 左で完結
        s -= 1
        t -= 1
    elif s >= a+2 and t > a+2:  # 右で完結
        s = s - (a+2)
        t = t - (a+2)
    else:  # 別れる
        if s < a+2 and t > a+2:  # Sが左tが右
            s -= 1
            t = t-(a+2)
            count += 1
        elif s > a+2 and t < a+2:  # sが右tが左
            s = s-(a+2)
            t -= 1
            count += 1
    k -= 1
ansewr = ""

moji = "ABC"
for _ in range(k-1):
    moji = "A" + moji + "B" + moji + "C"
if count==0:
    ansewr =  s_mae + moji[s-1:t] + t_usiro
else:
    ansewr = s_mae + moji[s-1:] + s_t + moji[:t] + t_usiro
print(ansewr)
