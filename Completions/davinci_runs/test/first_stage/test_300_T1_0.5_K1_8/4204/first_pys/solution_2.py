

def main():
    s = input()
    k = int(input())

    if len(s) == 1:
        print(s[0])
        return

    n = int(s[0])
    s = s[1:]
    for i in range(len(s)):
        n_next = int(s[i])
        if n == n_next:
            n += 1
        else:
            break

    if k <= n:
        print(k)
    else:
        days = 1
        k -= n
        while days < 5000000000000000:
            if k <= len(s) * n:
                print(s[(k - 1) // n])
                return
            else:
                k -= len(s) * n
                days += 1
                n *= 2

        print(s[(k - 1) // n])

if __name__ == '__main__':
    main()