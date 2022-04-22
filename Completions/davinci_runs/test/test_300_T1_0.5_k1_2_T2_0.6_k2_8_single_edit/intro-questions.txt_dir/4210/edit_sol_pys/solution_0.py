# Solution 1
def is_valid(s):
    try:
        s = int(s)
        return True
    except:
        return False



def check_valid(num):
    num = str(num)
    if len(num) < 2:
        return False

    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            return False

    return True


def solve(s):
    if not is_valid(s):
        return -1

    s = int(s)
    if check_valid(s):
        return s

    s = str(s)
    res = -1
    for i in range(len(s) - 1, -1, -1):
        if s[i] < s[i - 1]:
            s = s[:i - 1] + s[i - 1] + ''.join(sorted(s[i:]))
            res = s
            break

    return res


print(solve(input()))


# Solution 2
def is_valid(s):
    try:
        s = int(s)
        return True
    except:
        return False


def check_valid(num):
    num = str(num)
    if len(num) < 2:
        return False

    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            return False

    return True


def solve(s):
    if not is_valid(s):
        return -1

    s = int(s)
    if check_valid(s):
        return s

    s = str(s)
    res = -1
    for i in range(len(s) - 1, -1, -1):
        if s[i] < s[i - 1]:
            s = s[:i - 1] + s[i - 1] + ''.join(sorted(s[i:]))
            res = s
            break

    return res


print(solve(input()))


# Solution 3
n, k = map(int, input().split())
a = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(n):
        if i != j:
            num1 = str(a[i]) + str(a[j])
            num1 = int(num1)
            if num1 % k == 0:
                res += 1

print(res)

# Solution 4
n, k = map(int, input().split())
a = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(i + 1, n):
        num1 = str(a[i]) + str(a[j])
        num1 = int(num1)
        if num1 % k == 0:
            res += 1

print(res)


# Solution 5
n = int(input())

res = 1
for i in range(2, n + 1):
    res *= i

print(res)
