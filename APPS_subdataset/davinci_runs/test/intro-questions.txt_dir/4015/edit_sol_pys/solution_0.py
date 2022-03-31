
def main():
    n, m = map(int, input().split())
    moves = 0
    while n != m:
        if n > m or m % 2 == 1:
            print(-1)
            return
        if m % 3 == 0:
            m = m // 3
        else:
            m = m // 2
        moves += 1
    print(moves)


if __name__ == '__main__':
    main()
