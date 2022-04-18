
def main():
    n = int(input())
    if n % 25 == 0:
        print(0)
        return
    if n % 10 == 0 and n // 10 % 25 == 0:
        print(1)
        return
    n = str(n)
    l = len(n)
    if l == 1:
        print(-1)
        return
    if l == 2:
        if n[0] == '0':
            print(1)
            return
        if n[1] == '0':
            print(1)
            return
        print(-1)
        return
    if l == 3:
        if n[0] == '0' and n[1] == '0':
            print(1)
            return
        if n[1] == '0' and n[2] == '0':
            print(2)
            return
        if n[0] == '0' and n[2] == '0':
            print(2)
            return
        if n[0] == '0':
            print(1)
            return
        if n[1] == '0':
            print(1)
            return
        if n[2] == '0':
            print(1)
            return
        print(-1)
        return
    if l == 4:
        if n[0] == '0' and n[1] == '0' and n[2] == '0':
            print(1)
            return
        if n[1] == '0' and n[2] == '0' and n[3] == '0':
            print(2)
            return
        if n[0] == '0' and n[2] == '0' and n[3] == '0':
            print(2)
            return
        if n[0] == '0' and n[1] == '0' and n[3] == '0':
            print(2)
            return
        if n[0] == '0' and n[1] == '0':
            print(1)
            return
        if n[1] == '0' and n[2] == '0':
            print(1)
            return
        if n[2] == '0' and n[3] == '0':
            print(1)
            return
        if n[0] == '0' and n[2] == '0':
            print(1)
            return
        if n[0] == '0' and n[3] == '0':
            print(1)
            return
        if n[1] == '0' and n[3] == '0':
            print(1)
            return
        if n[0] == '0':
            print(1)
            return
        if n[1] == '0':
            print(1)
            return
        if n[2] == '0':
            print(1)
            return
        if n[3] == '0':
            print(1)
            return
    print(-1)

if __name__ == '__main__':
    main()
