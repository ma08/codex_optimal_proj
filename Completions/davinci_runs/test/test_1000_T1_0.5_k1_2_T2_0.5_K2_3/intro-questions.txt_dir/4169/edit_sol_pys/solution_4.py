# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 10:34:05 2019
从键盘输入学生的成绩，从小到大排序后输出
@author: kc
"""
#%%

def main():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    a.sort()
    for i in range(len(a)):
        print(a[i], end=' ')

if __name__ == '__main__':
    main()
