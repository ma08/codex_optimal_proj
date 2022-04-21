
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

def main():
    n = list(map(int, input()))
    l = len(n) - 1
    if l == 0 and n[l] % 25 == 0:
        print(0)
        return
    if l == 1 and (n[l] % 25 == 0 or (n[l] % 10 == 0 and n[l - 1] % 25 == 0)):
        print(1)
        return
    if l == 1:
        print(-1)
        return
    if l == 2:
        if n[l] % 100 == 0 and n[l - 1] % 25 == 0:
            print(1)
            return
        if n[l] % 100 % 25 == 0:
            print(2)
            return
        if n[l - 1] % 25 == 0:
            print(1)
            return
        print(-1)
        return
    s = 0
    moves = 0
    for i in range(l, -1, -1):
        s += n[i]
        if s % 25 == 0:
            moves += l - i
            s = 0
            l = i
    if s == 0:
        print(moves)
        return
    print(-1)

if __name__ == '__main__':
    main()
