
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

def main():
    n = input()
    n = int(n)
    if n % 25 == 0:
        print(0)
        return
    s = n
    moves = 1
    while s != 0:
        if s % 100 == 0:
            s //= 100
            moves += 1
        else:
            s %= 100
    print(moves)

if __name__ == '__main__':
    main()
