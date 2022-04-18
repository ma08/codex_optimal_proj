
N = int(input())
B = list(map(int,input().split()))
A = [0]*N

A[0] = B[0] #最初の要素の設定
A[-1] = B[-1] #最後の要素の設定

for i in range(1,N-1):
    A[i] = B[i] - A[i-1] #Aの各要素について、Bの各要素-Aの1つ前の要素を設定

print(sum(A))
