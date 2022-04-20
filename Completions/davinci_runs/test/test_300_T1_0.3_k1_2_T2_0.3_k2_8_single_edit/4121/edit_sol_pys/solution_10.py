
n = int(input())
a = list(map(int, input().split()))

def is_complete(a):
    return len(set(a)) == 1

def is_possible(a):
    if not is_complete(a):
        for i in range(n - 1):
            if a[i] == a[i + 1]:
                a[i] += 1
                a[i + 1] += 1
                if is_possible(a): return True
                a[i] -= 1
                a[i + 1] -= 1
        for i in range(n):
            if a[i] >= 2: 
                a[i] -= 2
                if is_possible(a): return True
                a[i] += 2
    return False

if is_possible(a):
    print("YES")
else:
    print("NO")
