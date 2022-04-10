

def main():
    n = int(input())
    moves = 0
    while n % 25 != 0:
        if n < 25:
            moves = -1
            break
        n = str(n)
        if n[-1] == '0':
            n = n[:-1]
        elif n[-2] == '0':
            n = n[:-2] + n[-1]
        else:
            n = n[:-2] + n[-1] + n[-2]
        n = int(n)
        moves += 1
    print(moves)

if __name__ == "__main__":
    main()