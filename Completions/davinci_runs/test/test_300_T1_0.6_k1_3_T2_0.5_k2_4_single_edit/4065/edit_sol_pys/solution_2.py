

m = int(input())
a = list(map(int, input().split()))  # a = [1, 2, 3, 4, 5]

q = [a[0]]  # q = [1]
for i in range(1, m):
    if a[i] <= 2 * q[-1]:  # 5 <= 2 * 1
        q[-1] = a[i]  # q = [5]
    else:
        q.append(a[i])

print(len(q))
