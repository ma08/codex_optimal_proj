
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

def main():
    n = input()
    n = int(n)
    s = n
    moves = 0
    while s % 25 == 0:
        moves += 1
        s //= 25
    if moves == 0:
        print(-1)
        return
    if s == 1:
        print(0)
        return
    print(moves + 1)

if __name__ == '__main__':
    main()
