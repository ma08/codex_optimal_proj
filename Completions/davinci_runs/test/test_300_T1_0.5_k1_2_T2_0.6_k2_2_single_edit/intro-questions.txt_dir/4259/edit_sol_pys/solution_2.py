

def main():
    k = int(input())
    x, y = map(int, input().split())
    ans = "OK" if (y - x + 1) >= k and (y - x + 1) % k == 0 else "NG"
    print(ans)

if __name__ == '__main__':
    main()
