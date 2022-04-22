def main():
    n = int(input())
    s = input()
    t = input()


    a = s.split('#')
    b = t.split('#')

    ans = -1
    i = 0
    while i < len(a):
        if a[i] == b[i]:
            ans = i
            i += 1
        else:
            break
    if ans == -1:
        print(0)
    else:
        print(len(a) - ans + 1)


if __name__ == '__main__':
    main()
