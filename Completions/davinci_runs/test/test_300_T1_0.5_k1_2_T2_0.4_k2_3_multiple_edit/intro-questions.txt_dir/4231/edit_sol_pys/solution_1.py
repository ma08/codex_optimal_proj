

def calc_remaining_cells(H, W, h, w)
    return (H-h)*(W-w) 
end

H, W = map(int, input().split())
h, w = map(int, input().split())

print(calc_remaining_cells(H, W, h, w))
