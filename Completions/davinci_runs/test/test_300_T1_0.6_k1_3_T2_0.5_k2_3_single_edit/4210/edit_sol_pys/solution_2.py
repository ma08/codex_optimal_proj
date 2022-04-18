def main():
    n = int(input())
    d = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += d[i] * d[j]
    print(ans)



if __name__ == "__main__":
    main()
