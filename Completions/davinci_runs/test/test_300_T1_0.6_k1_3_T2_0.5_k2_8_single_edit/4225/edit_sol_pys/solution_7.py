def f(a, b, c, k):
    if k <= a:
        return k
    elif a < k <= a + b:
        return a
    else:
        return a - (k - a - b)

def main():
    a, b, c, k = map(int, input().split())
    print(f(a, b, c, k))

if __name__ == '__main__':
    main()
