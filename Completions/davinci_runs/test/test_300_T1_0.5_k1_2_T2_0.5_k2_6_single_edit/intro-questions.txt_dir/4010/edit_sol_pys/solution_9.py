

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    n = int(input())
    for i in range(n):
        n = int(input())
        a = list(map(int, input().split()))
        if a[0] == a[-1]:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
