
def main():
    a, b, c, k = map(int, input().split())
    if k <= a:
        print(a - (k - a))
    elif a < k <= a + b:
        print(a)
    else:
        print(a - (k - a - b) * 2)

if __name__ == '__main__':
    main()
