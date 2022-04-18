

def main():
    n = int(input())
    languages = list(map(int, input().split()))
    awkwardness = n + 1
    for i in range(n):
        for j in range(i + 1, n):
            if languages[i] == languages[j]:
                awkwardness = min(awkwardness, j - i)
    if awkwardness == n + 1:
        print(-1)
    else:
        print(awkwardness)

if __name__ == "__main__":
    main()
