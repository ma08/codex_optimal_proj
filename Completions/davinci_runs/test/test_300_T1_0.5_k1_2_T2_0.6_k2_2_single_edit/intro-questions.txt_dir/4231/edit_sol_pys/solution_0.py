

def calc_remaining_cells(h, w):
    return (H-h)*(W-w) - (h*w)

H, W = map(int, input().split())
h, w = map(int, input().split())

print(calc_remaining_cells(h, w))
