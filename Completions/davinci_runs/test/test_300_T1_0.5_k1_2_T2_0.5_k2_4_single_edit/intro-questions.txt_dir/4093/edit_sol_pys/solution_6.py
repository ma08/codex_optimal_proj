

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        if n == 1:
            print(0)
        else:
            if m * 2 >= n:
                print(n - m * 2)
            else:
                print(m * 2 - n)

if __name__ == '__main__':
    main()
