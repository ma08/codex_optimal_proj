#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  file
#  
#  Copyright 2020 contributors of cardgame
#  
#  This file is part of cardgame.
#
#  cardgame is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  cardgame is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with cardgame.  If not, see <http://www.gnu.org/licenses/>.
#

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    A = [[int(x) for x in sys.stdin.readline().rstrip().split()] for _ in range(2)]  # noqa: E501
    dp = [[0] * N for _ in range(2)]
    dp[0][0] = A[0][0]
    dp[1][0] = A[1][0]
    for i in range(1, N):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1]) + A[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1]) + A[1][i]
    print(max(dp[0][N - 1], dp[1][N - 1]))

if __name__ == "__main__":
    main()
