# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-07 09:44:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-07 09:47:49


def main():
    k = int(input())
    if k == 1:
        print("1 0")
    else:
        i = 2
        while i < k:
            i *= 2
        print("%d %d" % (i, i//2 - 1))

if __name__ == "__main__":
    main()
