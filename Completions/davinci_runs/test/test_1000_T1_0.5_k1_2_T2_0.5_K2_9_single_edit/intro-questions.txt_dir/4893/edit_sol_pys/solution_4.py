

def main():
    n, p = map(int, input().split())
    dist = list(map(int, input().split()))
    dist.sort()

    i = 0
    while i < n - 1:
        if dist[i] + p * (i + 1) > dist[i + 1]:
            print(dist[i] + p * (i + 1))
            i = n
        else:
            i += 1
    if i == n - 1:
        print(dist[-1] + p * n)

if __name__ == "__main__":
    main()
