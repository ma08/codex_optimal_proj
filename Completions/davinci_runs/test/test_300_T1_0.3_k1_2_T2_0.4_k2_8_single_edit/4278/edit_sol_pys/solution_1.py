

import sys

def main():
    n = int(sys.stdin.readline())
    ss = []
    for i in range(n):
        ss.append(sys.stdin.readline().rstrip())
    ss.sort()
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if len(ss[i]) != len(ss[j]):
                continue
            if len(ss[i]) == len(set(ss[i])):
                continue
            if len(ss[j]) == len(set(ss[j])):
                continue
            if sorted(ss[i]) == sorted(ss[j]):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
