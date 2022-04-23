

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1 or a == 2 and b == 2 or b == 3 or b == 5 or b == 7 or b == 11 or a == 3 and b == 2 or b == 3 or b == 5 or b == 7 or b == 11 or a == 4 and b == 3 or b == 5 or b == 7 or b == 11 or a == 5 and b == 2 or b == 3 or b == 5 or b == 7 or b == 11 or a == 6 and b == 5 or b == 7 or b == 11 or a == 7 and b == 2 or b == 3 or b == 5 or b == 7 or b == 11 or a == 8 and b == 3 or b == 5 or b == 7 or b == 11 or a == 9 and b == 2 or b == 3 or b == 5 or b == 7:
        print(a * b)
    else:
        print(-1)


if __name__ == '__main__':
    main()
