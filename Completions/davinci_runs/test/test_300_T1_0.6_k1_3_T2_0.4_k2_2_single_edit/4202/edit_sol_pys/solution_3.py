

def main(a, b, n):
    x = min(b-1, n)
    print(a*x//b - a*(x//b))

if __name__ == "__main__":
    a, b, n = map(int, input().split())
    main(a, b, n)
