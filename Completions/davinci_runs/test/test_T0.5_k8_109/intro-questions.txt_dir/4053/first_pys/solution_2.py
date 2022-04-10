


def main():
    n = int(input())
    pre = []
    suf = []
    for i in range(2*n-2):
        s = input()
        if len(s) == 1:
            pre.append(i)
        else:
            suf.append(i)

    ans = ['P' if i in pre else 'S' for i in range(2*n-2)]
    print(''.join(ans))

if __name__ == "__main__":
    main()