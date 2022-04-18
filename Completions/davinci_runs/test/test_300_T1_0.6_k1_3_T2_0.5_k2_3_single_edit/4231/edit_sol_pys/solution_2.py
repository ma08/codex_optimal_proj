
import sys

H, W = map(int, sys.stdin.readline().split())
h, w = map(int, sys.stdin.readline().split())

chosen_rows = h * W

unchosen_rows = (H - h) * W

chosen_columns = w * H

unchosen_columns = (W - w) * H

print(chosen_rows + chosen_columns - unchosen_rows - unchosen_columns)
