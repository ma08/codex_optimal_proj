import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def main():
    S = input().strip()
    count = 0
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
