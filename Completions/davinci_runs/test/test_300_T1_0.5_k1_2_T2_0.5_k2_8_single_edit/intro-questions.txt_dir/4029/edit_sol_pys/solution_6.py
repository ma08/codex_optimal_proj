
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

def main():
    n = input()
    l = len(str(n))
    if l == 1 and int(n) % 25 == 0:
        print(0)
        return
    if l == 2 and (int(n) % 25 == 0 or (int(n) % 10 == 0 and int(n) // 10 % 25 == 0)):
        print(1)
        return
    if l == 2:
        print(-1)
        return
    if l == 3:
        if int(n) % 100 == 0 and int(n) // 100 % 25 == 0:
            print(1)
            return
        if int(n) % 100 % 25 == 0:
            print(2)
            return
        if int(n) // 100 % 25 == 0:
            print(1)
            return
        print(-1)
        return
    s = 0
    moves = 0
    for i in range(l - 1, -1, -1):
        s += int(n[i])
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
