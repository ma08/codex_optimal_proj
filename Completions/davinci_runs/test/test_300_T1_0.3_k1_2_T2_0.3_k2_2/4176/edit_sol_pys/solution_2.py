

def main():
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    ans = x
    while ans % y != 0:
        ans += x
    print(ans) 

if __name__ == '__main__':
    main()
