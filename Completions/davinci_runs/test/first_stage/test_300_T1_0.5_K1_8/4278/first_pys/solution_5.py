

import sys

def main():
    n = int(sys.stdin.readline())
    s = []
    for i in range(n):
        s.append(sys.stdin.readline().rstrip())
    
    t = []
    for i in range(n):
        t.append("".join(sorted(s[i])))
    t.sort()

    ans = 0
    for i in range(n-1):
        if t[i] == t[i+1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()