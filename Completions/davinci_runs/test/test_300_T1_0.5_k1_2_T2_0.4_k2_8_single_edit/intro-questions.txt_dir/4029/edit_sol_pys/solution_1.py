
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

def main():
    n = input()
    n = list(map(int, n))
    l = len(n)
    if l == 1 and n[0] % 25 == 0:
        print(0)
        return
    if l == 2 and (n[1] % 25 == 0 or (n[1] % 10 == 0 and n[0] % 25 == 0)):
        print(1)
        return
    if l == 2:
        print(-1)
        return
    if l == 3:
        if n[2] % 100 == 0 and n[1] % 25 == 0:
            print(1)
            return
        if n[2] % 100 % 25 == 0:
            print(2)
            return
        if n[1] % 25 == 0:
            print(1)
            return
        print(-1)
        return
    s = 0
    moves = 0
    for i in range(l - 1, -1, -1):
        s += n[i]
        if s % 25 == 0:
            moves += l - i
            s = 0
            l = i + 1
    if s == 0:
        print(moves)
        return
    print(-1)

if __name__ == '__main__':
    main()
