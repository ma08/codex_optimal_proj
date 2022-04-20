
def solve(n, q):
    a = [1]
    for i in range(n-1):
        if a[-1] + q[i] > 0 and a[-1] + q[i] <= n:
            a.append(a[-1] + q[i])
        else:
            return -1
    return a




def main():
    n = int(input())
    q = list(map(int, input().split()))
    print(*solve(n, q))


if __name__ == "__main__":
    main()
