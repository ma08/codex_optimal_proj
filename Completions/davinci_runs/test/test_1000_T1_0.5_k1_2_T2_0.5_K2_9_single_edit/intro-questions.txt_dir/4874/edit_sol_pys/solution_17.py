
import sys
sys.setrecursionlimit(10**6)
#----Solution----

def main():
    n, m = map(int, sys.stdin.readline().split())
    l = []
    count = 0
    for i in range(n):
        l.append(sys.stdin.readline())
    for i in range(m):
        if l[0][i] == '_':
            count += 1
    print(count)

main()
