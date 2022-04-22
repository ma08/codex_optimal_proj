import sys

import numpy as np

def main():
    sys.setrecursionlimit(10**6)
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "s":
                start_h = i
                start_w = j
    for i in range(H):
        for j in range(W):
            if S[i][j] == "g":
                goal_h = i
                goal_w = j
    visited = [[False] * W for _ in range(H)]
    visited[start_h][start_w] = True
    if dfs(start_h, start_w, goal_h, goal_w, visited, S):
        print("Yes")
    else:
        print("No")

def dfs(h, w, goal_h, goal_w, visited, S):
    if h == goal_h and w == goal_w:
        return True
    if h > 0 and not visited[h-1][w] and S[h-1][w] != "#":
        visited[h-1][w] = True
        if dfs(h-1, w, goal_h, goal_w, visited, S):
            return True
    if h < H-1 and not visited[h+1][w] and S[h+1][w] != "#":
        visited[h+1][w] = True
        if dfs(h+1, w, goal_h, goal_w, visited, S):
            return True
    if w > 0 and not visited[h][w-1] and S[h][w-1] != "#":
        visited[h][w-1] = True
        if dfs(h, w-1, goal_h, goal_w, visited, S):
            return True
    if w < W-1 and not visited[h][w+1] and S[h][w+1] != "#":
        visited[h][w+1] = True
        if dfs(h, w+1, goal_h, goal_w, visited, S):
            return True
    return False

if __name__ == "__main__":
    main()
