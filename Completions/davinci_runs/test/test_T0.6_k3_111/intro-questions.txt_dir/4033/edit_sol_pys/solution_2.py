

def main():
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    if b * 2 < a:
        ans = a + a + b + b
    else:
        ans = a + a + a + b
    print(ans)

if __name__ == '__main__':
    main()
