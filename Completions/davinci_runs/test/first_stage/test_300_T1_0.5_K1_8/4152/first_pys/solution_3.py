

n = int(input())
a = list(map(int, input().split()))

def is_power_of_two(n):
    return n != 0 and ((n & (n - 1)) == 0)

def is_good(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and is_power_of_two(a[i] + a[j]):
                return True
    return False

def get_min_bad(a):
    if is_good(a):
        return 0
    else:
        min_bad = len(a)
        for i in range(len(a)):
            if not is_good(a[:i] + a[i+1:]):
                min_bad = min(min_bad, 1 + get_min_bad(a[:i] + a[i+1:]))
        return min_bad

print(get_min_bad(a))