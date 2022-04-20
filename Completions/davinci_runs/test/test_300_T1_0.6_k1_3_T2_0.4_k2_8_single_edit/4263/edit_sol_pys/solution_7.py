

#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-08-03 15:12:42 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-08-03 15:12:42 

# AtCoder Beginner Contest 070
# Problem A

if __name__ == '__main__':
    n = int(input())
    if n % 10 == n // 100:
        print('Yes')
    else:
        print('No')
