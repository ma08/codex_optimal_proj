#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-22 10:41:31
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-22 10:41:40


def main():
    h, w = map(int, input().split())

    if h % 3 == 0 or w % 3 == 0:
        print(0)
        return

    if h > w:
        h, w = w, h

    min_diff = float('inf')
    for i in range(1, h):
        area_1 = i * w
        area_2 = (h - i) // 2 * w
        area_3 = (h - i) - area_2
        max_area = max(area_1, area_2, area_3)
        min_area = min(area_1, area_2, area_3)
        min_diff = min(min_diff, max_area - min_area)

    print(min_diff)


if __name__ == '__main__':
    main()
