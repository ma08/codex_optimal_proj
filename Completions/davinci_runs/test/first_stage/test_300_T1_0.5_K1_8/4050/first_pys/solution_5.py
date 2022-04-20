

n = int(input())
a = list(map(int, input().split()))

s = sum(a)

if s % n == 0:
    s = s // n
    count = 1
    b = []

    for i in range(n):
        if i == 0:
            b.append([a[i]])

        elif a[i] == s and sum(b[-1]) == s:
            count += 1
            b.append([a[i]])

        else:
            b[-1].append(a[i])

    print(count)
    for i in range(count):
        print(i + 1, i + 1)

else:
    print(1)
    print(1, n)