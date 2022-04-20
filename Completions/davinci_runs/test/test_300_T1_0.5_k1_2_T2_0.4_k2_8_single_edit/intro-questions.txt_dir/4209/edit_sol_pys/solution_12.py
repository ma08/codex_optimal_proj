import sys

def solve(a):
    ans = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                ans = max(ans, j - i)
    return ans

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(a))

if __name__ == '__main__':
    main()
