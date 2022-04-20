
import sys

def main():
    N = int(sys.stdin.readline())
    people = [[] for _ in range(N)]
    for i in range(N):
        A_i = int(sys.stdin.readline())
        for j in range(A_i):
            x_ij, y_ij = map(int, sys.stdin.readline().split())
            people[i].append((x_ij-1, y_ij))
    print(solve(people))

def solve(people):
    N = len(people)
    for i in range(2**N):
        if is_satisfied(people, i):
            return bin(i).count('1')
    return 0

def is_satisfied(people, i):
    for j in range(len(people)):
        if (i >> j) & 1:
            for x_ij, y_ij in people[j]:
                if (i >> (x_ij-1)) & 1 != y_ij:
                    return False
    return False

if __name__ == '__main__':
    main()
