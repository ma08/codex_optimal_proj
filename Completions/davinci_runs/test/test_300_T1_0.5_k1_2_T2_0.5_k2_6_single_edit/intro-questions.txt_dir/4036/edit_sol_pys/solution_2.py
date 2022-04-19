
def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    diff = [0] * n
    for i in range(n):
        diff[i] = a[i] - b[i]

    diff.sort()

    for i in range(n):
        if diff[i] > 0:
            diff[i] = -1
        else:
            diff[i] = 1

    print(diff)

    ans = 0
    for i in range(n):
        if diff[i] == 1:
            ans += 1
        else:
            if diff[i] == -1:
                if diff[i + 1] == -1:
                    diff[i] = 1
                    diff[i + 1] = 1
                    ans += 1
                else:
                    diff[i] = 1
                    diff[i + 1] = -1
                    ans += 1
            else:
                if diff[i + 1] == -1:
                    diff[i] = 1
                    diff[i + 1] = 1
                    ans += 1

    print(ans)

if __name__ == "__main__":
    main()
