

def main():
    k = int(input())
    a, b = map(int, input().split())
    ans = "OK" if (b - a) >= k and (b - a) % k == 0 else "NG" 
    print(ans)

if __name__ == '__main__':
    main()
