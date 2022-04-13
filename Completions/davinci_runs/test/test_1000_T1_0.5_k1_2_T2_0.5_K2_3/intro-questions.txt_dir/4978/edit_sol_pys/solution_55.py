#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:57:03 2020

@author: konrad
"""

def move(row, col, direction):
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    return (row, col)



def print_grid(grid):
    for row in grid:
        print("".join(row))


def main():
    N, M = map(int, input().split())
    grid = [list(input()) for _ in range(N)]
    for row in range(N):
        for col in range(M):
            if grid[row][col] == "V":
                if row == 0:
                    pass
                elif grid[row-1][col] == ".":
                    grid[row-1][col] = "V"
                elif grid[row-1][col] == "#":
                    if col > 0 and grid[row][col-1] == ".":
                        grid[row][col-1] = "V"
                    if col < M-1 and grid[row][col+1] == ".":
                        grid[row][col+1] = "V"
    print_grid(grid)


if __name__ == "__main__":
    main()
