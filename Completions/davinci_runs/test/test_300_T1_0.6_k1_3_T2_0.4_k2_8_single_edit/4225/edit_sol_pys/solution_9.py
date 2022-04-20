

def main():
    a, b, c, k = map(int, input().split())
    if k <= a:
        print(k)
    elif a < k <= a + b:  # ここに=をつける
        print(a)
    else:
        print(a - (k - a - b))  # ここに-をつける

if __name__ == '__main__':
    main()
