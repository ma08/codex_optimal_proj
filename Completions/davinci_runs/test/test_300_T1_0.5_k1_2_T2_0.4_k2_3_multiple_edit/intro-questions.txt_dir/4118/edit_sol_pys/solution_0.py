

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print(a * b)
    else:
        print(-1)

if __name__ == '__main__':
    main()
