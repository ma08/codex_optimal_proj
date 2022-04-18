

def main(n, d, c):
    result = [1] * n
    for i in d:
        result[i] = result[i] + 1
    for i in range(n):
        c[result[i] - 1] += 1
    print(" ".join(map(str,c)))

if __name__ == "__main__":
    n = int(input())
    d = list(map(int, input().split()))
    c = []
    main(n,d,c)
