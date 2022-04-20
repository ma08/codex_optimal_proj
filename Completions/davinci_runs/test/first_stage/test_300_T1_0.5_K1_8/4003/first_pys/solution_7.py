

import sys

def solve(a):
    n = len(a)
    l = []
    r = []
    for i in range(n):
        if l and a[i] <= l[-1]:
            l.append(a[i])
        else:
            l.append(l[-1])
        if r and a[n-i-1] <= r[-1]:
            r.append(a[n-i-1])
        else:
            r.append(r[-1])
    r = r[::-1]
    l = l[::-1]
    #print(l, r)
    ans = 0
    s = ""
    for i in range(n):
        if l[i] < r[i]:
            ans += 1
            s += 'L'
        elif l[i] > r[i]:
            ans += 1
            s += 'R'
        else:
            if i == n-1:
                ans += 1
                s += 'R'
            else:
                ans += 2
                s += 'LR'
    return ans, s

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans, s = solve(a)
    print(ans)
    print(s)

if __name__ == '__main__':
    main()