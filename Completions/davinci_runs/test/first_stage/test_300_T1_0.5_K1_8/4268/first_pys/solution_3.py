

def main():
    n, d = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            dist = 0
            for k in range(d):
                dist += (x[i][k] - x[j][k]) ** 2
            if dist ** 0.5 == int(dist ** 0.5):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()