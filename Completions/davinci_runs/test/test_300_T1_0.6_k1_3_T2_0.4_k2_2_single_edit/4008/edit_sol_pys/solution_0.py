import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    arr = list(map(int, input().split()))[::-1]
    ans = [0 for _ in range(n)]
    ans[0] = 1
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            ans[i] = ans[i - 1] + 1
        else:
            ans[i] = 1
    print(sum(ans))


if __name__ == "__main__":
    main('dance')
