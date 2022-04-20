

import sys

def main():
    n, r = [int(x) for x in raw_input().split()]
    projects = []
    for i in range(n):
        a, b = [int(x) for x in raw_input().split()]
        projects.append((a, b))
    projects.sort(key=lambda x: x[1])
    for p in projects:
        r += p[1]
        if r < p[0]:
            print "NO"
            return
    print "YES"

if __name__ == "__main__":
    main()