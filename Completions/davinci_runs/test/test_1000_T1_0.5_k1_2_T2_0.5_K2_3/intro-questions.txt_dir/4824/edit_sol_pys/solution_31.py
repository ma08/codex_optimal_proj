
import sys

def readline():
    return sys.stdin.readline().strip()

def main():
    N, K = [int(x) for x in readline().split()]
    groups = [int(x) for x in readline().split()]

    groups.sort()

    count = 0
    for i in range(N - 1):
        if groups[i] == groups[i+1]:
            count += 1
    print(count + 1)

if __name__ == '__main__':
    main()
