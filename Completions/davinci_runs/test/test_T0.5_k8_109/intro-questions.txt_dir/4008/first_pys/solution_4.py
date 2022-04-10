

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()

# print(n, k, a)

def check(a):
    for i in range(1, n):
        if a[i] == a[i-1]:
            return False
    return True

if check(a):
    print("YES")
    print(" ".join(str(i % k + 1) for i in range(n)))
else:
    print("NO")