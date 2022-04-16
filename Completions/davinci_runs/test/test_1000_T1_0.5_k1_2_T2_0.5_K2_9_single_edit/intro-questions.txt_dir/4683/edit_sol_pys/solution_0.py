

n = int(input())
l = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        ans += l[i] * l[j]
<<<<<<< HEAD

=======
print(ans % (10**9+7))
>>>>>>> c4e4a4eb4c4f4a2d6d9b6f8a6cdb8e4d43b84c4f
print(ans % (10**9+7))
