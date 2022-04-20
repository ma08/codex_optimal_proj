import sys

def min_moves(a, k):
    a.sort(reverse=True)
    moves = 0
    i = 0
    for i in range(len(a)):
        if a[i] == a[i + 1]:
            continue
        moves += len(a) - k
    return moves

def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(min_moves(a, k))

if __name__ == '__main__':
    main()
