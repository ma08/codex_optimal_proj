

import sys

def main():
    lines = sys.stdin.readlines()
    h, n, m = [int(x) for x in lines[0].split()]
    ans = [0, 0, 0]
    if h <= 1:
        print(" ".join([str(x) for x in ans[:2]]))
        return
    if h == 2:
        ans[0] = 1
        ans[1] = 2
        print(" ".join([str(x) for x in ans[:2]]))
        return
    if h == 3:
        ans[0] = 0
        ans[1] = 4
        print(" ".join([str(x) for x in ans[:2]]))
        return
    if h == 4:
        if n >= 2 and m >= 4:
            ans[0] = 2
            ans[1] = 4
            print(" ".join([str(x) for x in ans[:2]]))
            return
        if n >= 1 and m >= 6:
            ans[0] = 1
            ans[1] = 6
            print(" ".join([str(x) for x in ans[:2]]))
            return
        if n == 0 and m >= 8:
            ans[0] = 0
            ans[1] = 8
            print(" ".join([str(x) for x in ans[:2]]))
            return
    ans[2] = (h-4)*2
    ans[1] = 2 - n
    if ans[2] < 0:
        ans[1] = 2
        ans[2] = 0
    print(" ".join([str(x) for x in ans[:2]]))


if __name__ == '__main__':
    main()
