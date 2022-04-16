
#coding:utf-8
N, K = map(int, input().split())
S = input()
ans = ""
for i in S:
    if i == "A":
        ans += "A"
    elif i == "B":
        ans += "B"
    elif i == "C":
        ans += "C"
    else:
        if K > 0:
            ans += "A"
            K -= 1
        else:
            ans += "B"
print(ans)
