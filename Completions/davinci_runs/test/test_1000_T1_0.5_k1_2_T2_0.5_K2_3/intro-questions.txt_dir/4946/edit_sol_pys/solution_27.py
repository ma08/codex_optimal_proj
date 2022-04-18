

def main():
    n = int(input())
    languages = list(map(int, input().split()))
    awkwardness = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if languages[i] == languages[j]:
                awkwardness = min(awkwardness, j - i)
    print(awkwardness if awkwardness > 0 else -1)

if __name__ == "__main__":
    main()
