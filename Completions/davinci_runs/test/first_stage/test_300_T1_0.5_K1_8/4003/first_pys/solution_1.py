

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Pandas_Juice
# Team: Loitering
# Contest: Codeforces Round #637 (Div. 3)

def main():
    # n = int(input())
    # a = list(map(int, input().split()))
    n = 5
    a = [1, 2, 4, 3, 2]
    # n = 7
    # a = [1, 3, 5, 6, 5, 4, 2]
    # n = 3
    # a = [2, 2, 2]
    # n = 4
    # a = [1, 2, 4, 3]
    # print(n, a)
    # print(a[1:])
    # print(a[:2])
    # print(a[:-1])
    # print(a[1:])
    # print(a[:-1])
    # print(a[:-2])
    # print(a[1:])
    # print(a[:-1])
    # print(a[:-2])
    # print(a[:-3])
    # print(a[:-4])
    # print(a[:-5])
    # print(a[:-6])
    # print(a[:-7])
    # print(a[:-8])
    # print(a[:-9])
    # print(a[:-10])
    # print(a[-1:])
    # print(a[-2:])
    # print(a[-3:])
    # print(a[-4:])
    # print(a[-5:])
    # print(a[-6:])
    # print(a[-7:])
    # print(a[-8:])
    # print(a[-9:])
    # print(a[-10:])
    # print(a[1:])
    # print(a[:-1])
    # print(a[:-2])
    # print(a[:-3])
    # print(a[:-4])
    # print(a[:-5])
    # print(a[:-6])
    # print(a[:-7])
    # print(a[:-8])
    # print(a[:-9])
    # print(a[:-10])
    # print(a[-1:])
    # print(a[-2:])
    # print(a[-3:])
    # print(a[-4:])
    # print(a[-5:])
    # print(a[-6:])
    # print(a[-7:])
    # print(a[-8:])
    # print(a[-9:])
    # print(a[-10:])
    # print(a[1:])
    # print(a[:-1])
    # print(a[:-2])
    # print(a[:-3])
    # print(a[:-4])
    # print(a[:-5])
    # print(a[:-6])
    # print(a[:-7])
    # print(a[:-8])
    # print(a[:-9])
    # print(a[:-10])
    # print(a[-1:])
    # print(a[-2:])
    # print(a[-3:])
    # print(a[-4:])
    # print(a[-5:])
    # print(a[-6:])
    # print(a[-7:])
    # print(a[-8:])
    # print(a[-9:])
    # print(a[-10:])
    # print(a[1:])
    # print(a[:-1])
    # print(a[:-2])
    # print(a[:-3])
    # print(a[:-4])
    # print(a[:-5])
    # print(a[:-6])
    # print(a[:-7])
    # print(a[:-8])
    # print(a[:-9])
    # print(a[:-10])
    # print(a[-1:])
    # print(a[-2:])
    # print(a[-3:])
    # print(a[-4:])
    # print(a[-5:])
    # print(a[-6:])
    # print(a[-7:])
    # print(a[-8:])
    # print(a[-9:])
    # print(a[-10:])
    # print(a[1:])
    # print(a[:-1])
    # print(a[:-2])
    # print(a[:-3])
    # print(a[:-4])
    # print(a[:-5])
    # print(a[:-6])
    # print(a[:-7])
    # print(a[:-8])
    # print(a[:-9])
    # print(a[:-10])
    # print(a[-1:])
    # print(a[-2:])
    # print(a[-3:])
    # print(a[-4:])
    # print(a[-5:])
    # print(a[-6:])
    # print(a[-7:])
    # print(a[-8:])
    # print(a[-9:])
    # print(a[-10:])
    # print(a[1:])
    # print(a[:-1])
    # print(a[:-2])
    # print(a[:-3])
    # print(a[:-4])
    # print(a[:-5])
    # print(a[:-6])
    # print(a[:-7])
    # print(a[:-8])
    # print(a[:-9])
    # print(a[:-10])
    # print(a[-1:])
    # print(a[-2:])
    # print(a[-3:])
    # print(a[-4:])
    # print(a[-5:])
    # print(a[-6:])
    # print(a[-7:])
    # print(a[-8:])
    # print(a[-9:])
    # print(a[-10:])

    # 1 2 4 3 2
    # 1 2 4 3 2
    # 2 4 3 2
    # 2 4 3 2
    # 4 3 2
    # 4 3 2
    # 3 2
    # 3 2
    # 2
    # 2

    # 1 3 5 6 5 4 2
    # 1 3 5 6 5 4 2
    # 3 5 6 5 4 2
    # 3 5 6 5 4 2
    # 5 6 5 4 2
    # 5 6 5 4 2
    # 6 5 4 2
    # 6 5 4 2
    # 5 4 2
    # 5 4 2
    # 4 2
    # 4 2
    # 2
    # 2

    # 2 2 2
    # 2 2 2
    # 2 2
    # 2 2
    # 2
    # 2

    # 1 2 4 3
    # 1 2 4 3
    # 2 4 3
    # 2 4 3
    # 4 3
    # 4 3
    # 3
    # 3

    ans = []
    for i in range(len(a)):
        if i == 0:
            if a[i+1] > a[i]:
                ans.append('L')
            else:
                ans.append('R')
        elif i == len(a)-1:
            if a[i-1] > a[i]:
                ans.append('L')
            else:
                ans.append('R')
        else:
            if a[i-1] > a[i]:
                ans.append('L')
            else:
                ans.append('R')
    print(ans)
    print(len(ans))
    print(''.join(ans))

if __name__ == '__main__':
    main()