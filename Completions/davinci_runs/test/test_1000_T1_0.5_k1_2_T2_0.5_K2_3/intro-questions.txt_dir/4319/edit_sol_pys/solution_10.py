
from sys import stdin

def main():
    n = int(stdin.readline())
    a = stdin.readline().split()
    a = [int(x) for x in a]
    i = 0
    stairways = 1
    steps = []
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        stairways += 1
        steps.append(a[i])
        i = j
    print(stairways)
    print(*steps)

if __name__ == '__main__':
    main()
