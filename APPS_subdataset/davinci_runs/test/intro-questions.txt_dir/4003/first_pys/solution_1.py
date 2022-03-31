


def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = []
    r = []
    ans = []
    while a:
        if not l:
            l.append(a.pop(0))
            ans.append('L')
        elif not r:
            r.append(a.pop())
            ans.append('R')
        elif l[-1] < r[-1]:
            r.append(a.pop())
            ans.append('R')
        elif l[-1] < a[0]:
            l.append(a.pop(0))
            ans.append('L')
        elif r[-1] < a[-1]:
            r.append(a.pop())
            ans.append('R')
        else:
            break
    print(len(l) + len(r))
    print(''.join(ans))


if __name__ == '__main__':
    main()