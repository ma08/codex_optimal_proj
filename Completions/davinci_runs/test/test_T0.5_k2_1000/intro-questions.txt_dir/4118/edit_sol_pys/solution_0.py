

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1 or a == 2 or b == 2 or a == 3 or b == 3 or a == 5 or b == 5 or a == 7 or b == 7 or a == 11 or b == 11:
        print(a * b)
    else:
        print(-1)

if __name__ == '__main__':
    main()
