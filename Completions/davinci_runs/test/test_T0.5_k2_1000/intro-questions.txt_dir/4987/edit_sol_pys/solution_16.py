
import sys

def main():
    S, C, K = [int(i) for i in sys.stdin.readline().split()]
    D = [int(i) for i in sys.stdin.readline().split()]
    D.sort()
    i = 0
    count = 0
    while i < S:
        count += 1
        j = i + 1
        while j < S and D[j] - D[i] <= K and j - i + 1 <= C:
            j += 1
        i = j
    print(count)

if __name__ == '__main__':
    main()
