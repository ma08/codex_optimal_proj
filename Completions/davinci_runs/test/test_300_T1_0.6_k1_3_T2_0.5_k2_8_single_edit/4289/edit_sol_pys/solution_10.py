# ABC086A

n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

index = 0
diff = 10000

for i in range(n):
    if abs(a - (t - h[i] * 0.006)) < diff:
        diff = abs(a - (t - h[i] * 0.006))
        index = i + 1


# ABC081A
print(input().count("1"))

# ABC081B
n = int(input())
a = list(map(int, input().split()))

count = 0

while all(i % 2 == 0 for i in a):
    a = list(map(lambda x: x / 2, a))
    count += 1

print(count)

# ABC081B
n = int(input())
a = list(map(int, input().split()))

count = 0

while all(i % 2 == 0 for i in a):
    a = list(map(lambda x: x / 2, a))
    count += 1

print(count)

# ABC083B
n, a, b = map(int, input().split())

sum_of_digits = 0

for i in range(1, n + 1):
    total = 0
    for j in str(i):
        total += int(j)
    if a <= total <= b:
        sum_of_digits += i

print(sum_of_digits)

# ABC085B
n = int(input())
d = [int(input()) for _ in range(n)]

print(len(set(d)))

# ABC085C
n, y = map(int, input().split())

for i in range(n + 1):
    for j in range(n - i + 1):
        k = n - i - j
        if 10000 * i + 5000 * j + 1000 * k == y:
            print(i, j, k)
            exit()

print("-1 -1 -1")

# ABC086C
n = int(input())

for _ in range(n):
    t, x, y = map(int, input().split())

    # tが偶数の場合
    if t % 2 == 0:
        # x + yが偶数の場合
        if (x + y) % 2 == 0:
            print("Yes")
        # x + yが奇数の場合
        else:
            print("No")

    # tが奇数の場合
    else:
        # x + yが偶数の場合
        if (x + y) % 2 == 0:
            print("No")
        # x + yが奇数の場合
        else:
            # x + yが奇数でt以上の場合
            if x + y <= t:
                print("Yes")
            # x + yが奇数でt未満の場合
            else:
                print("No")

# ABC087B
a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0

for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            if 500 * i + 100 * j + 50 * k == x:
                count += 1

print(count)

# ABC088B
n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
alice = 0
bob = 0

for i in range(n):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]

print(alice - bob)

# ABC088B
n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
alice = 0
bob = 0

for i in range(n):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]

print(alice - bob)
print(index)
