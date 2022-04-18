
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:13:08 2018

@author: zhanghuangzhao
"""

import sys

def main():
    n, b, a = map(int, input().split())
    s = list(map(int, input().split()))
    
    max_segments = 0
    cur_a = a
    cur_b = b
    for i in range(n):
        if s[i] == 1:
            if cur_b > 0:
                cur_b -= 1
                cur_a += 1
                if cur_a > a:
                    cur_a = a
            else:
                cur_a -= 1
        else:
            if cur_a > 0:
                cur_a -= 1
            else:
                cur_b -= 1
        if cur_a == 0 and cur_b == 0:
            break
        max_segments += 1
    print(max_segments)
    
if __name__ == "__main__":
    sys.exit(main())
