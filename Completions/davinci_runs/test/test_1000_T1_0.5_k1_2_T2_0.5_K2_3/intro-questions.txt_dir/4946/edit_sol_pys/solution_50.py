

def main():
    n = int(input())
    languages = list(map(int, input().split()))
    awkwardness = 0
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            if languages[i] == languages[j + 1]:
                awkwardness = min(awkwardness, j + 1 - i)
    print(awkwardness if awkwardness > 0 else -1)

if __name__ == "__main__":
    main()
