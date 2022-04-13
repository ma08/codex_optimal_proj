

#N = int(input())
#B = list(map(int,input().split()))


#A = [0]*N #Aの要素数をNに設定

#A[0] = B[0] #最初の要素の設定
#A[-1] = B[-1] #最後の要素の設定

#for i in range(1,N-1):
#    A[i] = B[i] - A[i-1] #Aの各要素について、Bの各要素-Aの1つ前の要素を設定

#print(sum(A))


N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = [0]*(N+M)

for i in range(N+M):
    if i < N:
        ans[i] = A[i]
    else:
        ans[i] = B[i-N]

ans.sort(reverse=True)

ans_sum = sum(ans[:K])

print(ans_sum)
