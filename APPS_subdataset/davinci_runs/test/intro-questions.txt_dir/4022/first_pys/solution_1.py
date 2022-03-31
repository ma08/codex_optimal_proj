


def main():
    n = int(input())
    seq = []
    for i in range(n):
        line = [int(x) for x in input().split()]
        seq.append(line)
    seq.sort(key=lambda x: x[1])
    ans = 0
    for i in range(n):
        if i == 0:
            ans = max(ans, seq[i][1] - seq[i+1][0])
        elif i == n-1:
            ans = max(ans, seq[i][0] - seq[i-1][1])
        else:
            ans = max(ans, seq[i][0] - seq[i-1][1])
            ans = max(ans, seq[i][1] - seq[i+1][0])
    print(ans)


if __name__ == '__main__':
    main()