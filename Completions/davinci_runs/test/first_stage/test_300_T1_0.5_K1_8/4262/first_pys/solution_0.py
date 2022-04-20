
import itertools

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    perms = list(itertools.permutations(range(1, N + 1)))
    print(abs(perms.index(tuple(P)) - perms.index(tuple(Q))))

if __name__ == '__main__':
    main()