
import numpy as np

def calc_remaining_cells(h, w):
    return (H-h+1)*(W-w+1)

H, W = map(int, input().split())
h, w = map(int, input().split())

print(calc_remaining_cells(H, W, h, w))
