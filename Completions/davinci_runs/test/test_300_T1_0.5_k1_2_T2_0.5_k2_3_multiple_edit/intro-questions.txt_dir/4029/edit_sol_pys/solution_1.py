
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

def main():
    n = input()
    n = int(n)
    n = str(n)
    m = len(str(n))
    if m == 1 and n % 25 == 0:
        print(0)
        return
    if m == 2 and (n % 25 == 0 or (int(n) % 10 == 0 and int(n) // 10 % 25 == 0)):
        print(1)
        return
    if m == 2:
        print(-1)
        return
    if m == 3:
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
    for i in range(m - 1, -1, -1):
        s += int(n[i])
        if s % 25 == 0:
            moves += m - i
            s = 0
            m = i + 1
    if s == 0:
        print(moves)
        return
    print(-1)

if __name__ == '__main__':
    main()
