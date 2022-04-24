

def main():
    a, b, h = map(int, input().split())
    if h >= a:
        ans = b
    else:
        ans = b - (a - h)
    print(ans)

if __name__ == '__main__':
    main()
