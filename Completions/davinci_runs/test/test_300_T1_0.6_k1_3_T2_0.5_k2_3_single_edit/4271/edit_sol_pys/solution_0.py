

n = input()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

ans = 0

for i in range(len(a)):
    ans += b[a[i]-1]
    if i != 0 and a[i] == a[i-1] + 1: #現在の料理が直前の料理と隣接していたら、その料理の組み合わせボーナスを足す
        ans += c[a[i-1]-1]

print(ans)
