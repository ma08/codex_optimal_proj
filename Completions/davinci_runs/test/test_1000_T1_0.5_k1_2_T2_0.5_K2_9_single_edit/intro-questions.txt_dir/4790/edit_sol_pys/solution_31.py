

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    score = 0
    for i in range(n):
        score += b[a[i] - 1]
        if i > 0 and a[i] - a[i-1] == 1:
            score += c[a[i-1] - 1]
    print(score)

if __name__ == "__main__":
    main()
