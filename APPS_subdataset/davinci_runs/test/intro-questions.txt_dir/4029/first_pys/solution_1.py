

def main():
    n = int(input())
    if n % 25 == 0:
        print(0)
        return
    s = str(n)
    moves = 0
    for i in range(1, len(s)):
        if s[i] == '0':
            if s[i - 1] == '0':
                moves += 1
            else:
                moves += 2
    if s[-1] == '0':
        moves += 1
    elif s[-2] == '0':
        moves += 2
    else:
        moves = -1
    print(moves)

if __name__ == '__main__':
    main()