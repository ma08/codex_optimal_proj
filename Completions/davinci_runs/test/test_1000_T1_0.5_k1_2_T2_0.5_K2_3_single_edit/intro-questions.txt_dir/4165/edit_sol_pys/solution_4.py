
N = int(input())
L = list(map(int, input().split()))

L.sort()

if L[0] + L[1] > L[-1]:  # 全ての辺の長さを満たすとき
    print("Yes")
else:  # 全ての辺の長さを満たさないとき
    print("No")
