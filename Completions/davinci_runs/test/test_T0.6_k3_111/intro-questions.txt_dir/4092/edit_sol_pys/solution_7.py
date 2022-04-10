
def solve(n, a):
    count = 0
    s = 0
    h = {0: -1}
    for i in range(n):
        s += a[i]
        if s in h:
            count += i - h[s]
        h[s] = i

    return count

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))


if __name__ == '__main__':
    main()
