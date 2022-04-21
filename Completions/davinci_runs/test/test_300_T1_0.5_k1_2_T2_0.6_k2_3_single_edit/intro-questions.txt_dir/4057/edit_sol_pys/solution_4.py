

n = int(input())
a = list(map(int, input().split()))

a.sort()

def calc_max(a):
    max_a = a[-1]
    for i in range(n - 2, -1, -1):
        if max_a == a[i]:
            max_a += 1
            if max_a == a[i - 1]:
                max_a += 1
                if max_a == a[i - 2]:
                    max_a += 1
                    if max_a == a[i - 3]:
                        max_a += 1
        else:
            break
    return max_a

def calc_min(a):
    min_a = a[0]
    for i in range(n - 1):
        if min_a == a[i + 1]:
            min_a += 1
            if min_a == a[i + 2]:
                min_a += 1
                if min_a == a[i + 3]:
                    min_a += 1
                    if min_a == a[i + 4]:
                        min_a += 1
        else:
            break
    return min_a

print(calc_max(a) - calc_min(a) + 1)
