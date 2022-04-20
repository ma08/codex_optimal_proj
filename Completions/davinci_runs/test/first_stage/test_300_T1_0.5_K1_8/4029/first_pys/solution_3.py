


def main():
    n = input()
    moves = 0
    for i in range(len(n) - 2, -1, -1):
        if n[i] != '0':
            moves += int(n[i]) // 2
            n = n[:i] + n[i + 1:]
        else:
            moves += 1
            n = n[:i] + n[i + 1:]
    if n[-1] == '0':
        print(-1)
    else:
        print(moves)


if __name__ == '__main__':
    main()