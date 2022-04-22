

def main():
    k = int(input())
    a, b = map(int, input().split())
    print("OK" if (b - a + 1) >= k and (b - a + 1) % k == 0 else "NG")

if __name__ == '__main__':
    main()
