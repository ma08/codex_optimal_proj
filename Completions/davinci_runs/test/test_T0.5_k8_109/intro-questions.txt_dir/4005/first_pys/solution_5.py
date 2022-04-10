

def check_overlap(a, b):
    if a[1] < b[0] or a[0] > b[1]:
        return False
    else:
        return True

def check_overlap_x(a, b):
    if a[3] < b[2] or a[2] > b[3]:
        return False
    else:
        return True

def check_overlap_y(a, b):
    if a[0] < b[1] or a[1] > b[0]:
        return False
    else:
        return True

def check_overlap_xy(a, b):
    if a[0] < b[1] or a[1] > b[0]:
        return False
    elif a[3] < b[2] or a[2] > b[3]:
        return False
    else:
        return True


def check_overlap_x_y(a, b):
    if a[0] < b[1] or a[1] > b[0]:
        return False
    elif a[3] < b[2] or a[2] > b[3]:
        return False
    else:
        return True

def main():
    white_sheet = [int(x) for x in input().split()]
    black_sheet1 = [int(x) for x in input().split()]
    black_sheet2 = [int(x) for x in input().split()]
    #white_sheet = [3, 3, 7, 5]
    #black_sheet1 = [0, 0, 4, 6]
    #black_sheet2 = [0, 0, 7, 4]
    #white_sheet = [5, 2, 10, 5]
    #black_sheet1 = [3, 1, 7, 6]
    #black_sheet2 = [8, 1, 11, 7]
    #white_sheet = [0, 0, 1000000, 1000000]
    #black_sheet1 = [0, 0, 499999, 1000000]
    #black_sheet2 = [500000, 0, 1000000, 1000000]
    if check_overlap(black_sheet1, black_sheet2):
        if check_overlap_xy(white_sheet, black_sheet1) and check_overlap_xy(white_sheet, black_sheet2):
            print("NO")
        else:
            print("YES")
    else:
        if check_overlap_xy(white_sheet, black_sheet1) and check_overlap_xy(white_sheet, black_sheet2):
            print("NO")
        else:
            print("YES")

if __name__ == '__main__':
    main()