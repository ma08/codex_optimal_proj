def main():
    n = int(input())

    if n == 1:
        print(0)
        exit()

    moves = 0

    while n > 1:
        moves += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n += 1

    print(moves)

if __name__ == '__main__':
    main()
