
#import sys
#sys.stdin = open("input.txt", "r")

n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]

for cx in range(101):
    for cy in range(101):
        h = xyh[0][2] + abs(cx - xyh[0][0]) + abs(cy - xyh[0][1]) # 初期値
        if all(h - abs(cx - x[0]) - abs(cy - x[1]) == x[2] for x in xyh): # 初期値からそれぞれのhを求めて、全てのhが一致するか
            print(cx, cy, h) # 一致するならそれが答え
