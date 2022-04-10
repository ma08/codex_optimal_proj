

def check(a,n,k):
    if sum(a) != n:
        return False
    for i in a:
        if i == 0:
            return False
    for i in range(k-1):
        if a[i+1] > 2*a[i] or a[i+1] == a[i]:
            return False
    return True

n,k = [int(x) for x in input().split()]

if n == 1:
    print("YES\n1")
elif k == 1:
    print("NO")
elif k == 2:
    if n % 2 == 0:
        print("YES\n{} {}".format(n//2,n//2))
    else:
        print("NO")
elif k == 3:
    if n % 3 == 0:
        print("YES\n{} {} {}".format(n//3,n//3,n//3))
    else:
        print("NO")
elif k == 4:
    if n % 4 == 0:
        print("YES\n{} {} {} {}".format(n//4,n//4,n//4,n//4))
    elif n % 4 == 1:
        print("YES\n1 {} {} {}".format(n//4,n//4,n//4+1))
    elif n % 4 == 2:
        print("YES\n1 1 {} {}".format(n//4,n//4+1))
    elif n % 4 == 3:
        print("YES\n1 2 {} {}".format(n//4,n//4+1))
else:
    a = [1]*k
    for i in range(k):
        a[i] = i+1
        if check(a,n,k):
            break
        a[i] = i+2
        if check(a,n,k):
            break
    if check(a,n,k):
        print("YES")
        print(*a)
    else:
        print("NO")