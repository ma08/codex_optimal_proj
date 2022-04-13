

def main():
    n, p = map(int, input().split())
    dist = list(map(int, input().split()))
    dist.sort()

    for i in range(n - 1):  # n-1回ループ
        if dist[i] + p * (n - i - 1) > dist[i + 1]:
            print(dist[i] + p * (n - i - 1))
            break
    else:
        print(dist[-1] + p * (n + 1))

if __name__ == "__main__":
    main()
