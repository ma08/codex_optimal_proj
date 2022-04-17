
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

def main():
    s = input()
    l = len(s)
    if l == 1 and int(s) % 25 == 0:
        print(0)
        return
    if l == 2 and (int(s) % 25 == 0 or (int(s) % 10 == 0 and int(s) // 10 % 25 == 0)):
        print(1)
        return
    if l == 2:
        print(-1)
        return
    if l == 3:
        if int(s) % 100 == 0 and int(s) // 100 % 25 == 0:
            print(1)
            return
        if int(s) % 100 % 25 == 0:
            print(2)
            return
        if int(s) // 100 % 25 == 0:
            print(1)
            return
        print(-1)
        return
    ss = 0
    moves = 0
    for i in range(l - 1, -1, -1):
        ss += int(s[i])
        if ss % 25 == 0:
            moves += l - i
            ss = 0
            l = i + 1
    if ss == 0:
        print(moves)
        return
    print(-1)

if __name__ == '__main__':
    main()
