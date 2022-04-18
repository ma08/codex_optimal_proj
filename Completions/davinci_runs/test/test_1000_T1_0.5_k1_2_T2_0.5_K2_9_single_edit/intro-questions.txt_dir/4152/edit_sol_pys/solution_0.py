

# Solution 1

def solution1(n, a):
    s = set()
    for i in range(n):
        if a[i] not in s:
            s.add(a[i])
        else:
            s.remove(a[i])

    return n-len(s)

# Solution 2

def solution2(n, a):
    s = set()
    for i in range(n):
        if a[i] in s:
            s.remove(a[i])
        else:
            s.add(a[i])

    return n-len(s)

# Solution 3

def solution3(n, a):
    s = set()
    for i in range(n):
        s.add(a[i])

    return n-len(s)


n = int(input("Enter n: "))
a = list(map(int, input("Enter array: ").split()))

print("Solution 1: ", solution1(n, a))
print("Solution 2: ", solution2(n, a))
print("Solution 3: ", solution3(n, a))
