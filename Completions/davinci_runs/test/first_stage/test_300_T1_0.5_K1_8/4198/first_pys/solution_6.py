

def main():
    a, b, x = map(int, input().split())
    n = 0
    while True:
        if a * n + b * len(str(n)) > x:
            break
        n += 1
    print(n - 1)

if __name__ == '__main__':
    main()