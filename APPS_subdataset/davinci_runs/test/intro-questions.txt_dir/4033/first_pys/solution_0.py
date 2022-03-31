

def main():
    """
    a = 4
    b = 4
    """
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    if a > b * 2:
        ans = a + a + b + b
    else:
        ans = a + a + a + b
    print(ans)

if __name__ == '__main__':
    main()