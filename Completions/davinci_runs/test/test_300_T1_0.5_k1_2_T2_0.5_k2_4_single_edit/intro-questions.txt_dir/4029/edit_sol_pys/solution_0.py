
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

def main():
    s = input()
    s = int(s)
    l = len(s)
    if l == 1 and s % 25 == 0:
        print(0)
        return
    if l == 2 and (s % 25 == 0 or (s % 10 == 0 and s // 10 % 25 == 0)):
        print(1)
        return
    if l == 2:
        print(-1)
        return
    if l == 3:
        if s % 100 == 0 and s // 100 % 25 == 0:
            print(1)
            return
        if s % 100 % 25 == 0:
            print(2)
            return
        if s // 100 % 25 == 0:
            print(1)
            return
        print(-1)
        return
    n = 0
    moves = 0
    for i in range(l - 1, -1, -1):
        n += s[i]
        if n % 25 == 0:
            moves += l - i
            n = 0
            l = i + 1
    if n == 0:
        print(moves)
        return
    print(-1)

if __name__ == '__main__':
    main()
