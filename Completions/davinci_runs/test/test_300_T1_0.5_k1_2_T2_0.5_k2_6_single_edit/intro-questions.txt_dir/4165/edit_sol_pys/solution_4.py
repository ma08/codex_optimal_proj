
N = int(input())
L = list(map(int, input().split())) # 入力を数値に変換してリストにする

L.sort()

if L[0] + L[1] > L[-1]: # 三角形の成立条件
    print("Yes")
else:
    print("No")
