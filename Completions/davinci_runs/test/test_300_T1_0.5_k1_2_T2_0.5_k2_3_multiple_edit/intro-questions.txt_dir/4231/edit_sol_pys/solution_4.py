

def calc_remaining_cells(h, w, H, W):
    return (h-H)*(w-W)

h, w = map(int, input().split()) # input height and width
H, W = map(int, input().split()) # input height and width of black blocks

print(calc_remaining_cells(h, w, H, W))
