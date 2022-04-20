import copy

n = int(input())
a = list(map(int, input().split()))

#print(n)
#print(a)

def is_complete(a):
    if len(set(a)) == 1:
        return True
    else:
        return False

    b = copy.copy(a)
def is_possible(a):
    if is_complete(a):
        return True
    else:
        for i in range(n-1):
            if a[i] == a[i+1]:
                b[i] += 1
                b[i+1] += 1
                if is_possible(b):
                    return True
                else:
                    b[i] -= 1
                    b[i+1] -= 1
        for i in range(n):
            if b[i] >= 2:
                b[i] -= 2
                if is_possible(b):
                    return True
                else:
                    b[i] += 2
        return False

if is_possible(a):
    print("YES")
else:
    print("NO")
