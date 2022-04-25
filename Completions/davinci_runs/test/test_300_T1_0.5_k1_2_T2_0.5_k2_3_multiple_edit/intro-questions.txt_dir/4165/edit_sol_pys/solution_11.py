
N = int(input())
L = list(map(int, input().split())) # スペース区切りの整数の入力

L.sort()

if L[0] + L[1] > L[-1]:
    print("Yes")
else:
    print("No")
