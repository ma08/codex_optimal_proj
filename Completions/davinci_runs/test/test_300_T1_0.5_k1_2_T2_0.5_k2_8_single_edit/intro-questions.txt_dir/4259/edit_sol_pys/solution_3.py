

def main():
    k = int(input())
    a, b = map(int, input().split())
    ans = "OK" if (b - a + 1) >= k and (b - a + 1) % k == 0 else "NG" # NGとなるケースはkが大きい場合と、kが小さい場合
    print(ans)

if __name__ == '__main__':
    main()
