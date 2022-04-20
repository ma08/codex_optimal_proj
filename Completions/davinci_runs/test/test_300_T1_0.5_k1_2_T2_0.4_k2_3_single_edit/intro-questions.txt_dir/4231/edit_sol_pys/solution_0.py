

def calc_remaining_cells(h, w, H, W):
    return (h-H)*(w-W)

h, w = map(int, input().split()) # H, W
H, W = map(int, input().split()) # h, w

print(calc_remaining_cells(H, W, h, w))
