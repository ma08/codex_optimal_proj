
def calc_remaining_cells(height, width, h, w):
    return (height-h)*(width-w)

height, width = map(int, input().split())
h, w = map(int, input().split())

print(calc_remaining_cells(height, width, h, w))
