

def main():
    n, r = map(int, input().split())
    for _ in range(n):
        a, b = map(int, input().split())
        if r < a:
            print("NO")
            return
        r += b
    print("YES")

if __name__ == '__main__':
    main()