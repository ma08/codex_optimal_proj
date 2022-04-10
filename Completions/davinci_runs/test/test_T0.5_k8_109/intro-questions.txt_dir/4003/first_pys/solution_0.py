

import sys

def main():
    n = int(sys.stdin.readline().strip())
    s = [int(i) for i in sys.stdin.readline().strip().split()]
    l = r = 0
    a = []
    b = []
    while l < n and r < n:
        if s[l] < s[r]:
            a.append(s[l])
            l += 1
        else:
            b.append(s[r])
            r += 1
    a.extend(s[l:])
    b.extend(s[r:])
    a.reverse()
    b.reverse()
    #print(a, b)
    m = min(len(a), len(b))
    for i in range(m):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    #print(a, b)
    k = len(a) + len(b)
    if k == 0:
        print("1")
        print("R")
        return
    print(k)
    for i in range(len(a)):
        print("L", end="")
    for i in range(len(b)):
        print("R", end="")
    print()

if __name__ == "__main__":
    main()