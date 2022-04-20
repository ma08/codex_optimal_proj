

def main():
    a, b = map(int, input().split())
    if a > 20 or a < 1 or b > 20 or b < 1:
        print(-1)
        return
    print(a * b)

if __name__ == '__main__':
    main()
