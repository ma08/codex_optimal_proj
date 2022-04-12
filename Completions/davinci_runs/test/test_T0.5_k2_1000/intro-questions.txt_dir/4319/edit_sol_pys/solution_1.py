
import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    i = 0
    stairways_count = 1
    steps = []
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        steps.append(a[i])
        stairways_count += 1
        i = j
    print(stairways_count)
    print(*steps)

if __name__ == '__main__':
    main()
