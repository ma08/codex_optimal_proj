#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  file.py
#
#  Copyright 2020 Junli Zhang <zhjl86@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


def search(A, d, visited):
    if sum(visited) == len(visited):
        return 1
    ret = 0
    for i in range(len(A)):
        if visited[i] == 0 and A[d][i] == 1:
            visited[i] = 1
            ret += search(A, i, visited)
            visited[i] = 0

    return ret

def main():
    N, M = map(int, input().split())
    A = [[0]*N for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        A[a-1][b-1] = 1
        A[b-1][a-1] = 1
    visited = [0] * N
    visited[0] = 1
    print(search(A, 0, visited))


if __name__ == '__main__':
    main()
