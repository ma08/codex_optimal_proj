

def main():
    white_sheet_x1, white_sheet_y1, white_sheet_x2, white_sheet_y2 = map(int, input().split())
    black_sheet_1_x1, black_sheet_1_y1, black_sheet_1_x2, black_sheet_1_y2 = map(int, input().split())
    black_sheet_2_x1, black_sheet_2_y1, black_sheet_2_x2, black_sheet_2_y2 = map(int, input().split())

    if white_sheet_x1 == black_sheet_1_x1 and white_sheet_x2 == black_sheet_1_x2 and white_sheet_y1 == black_sheet_1_y1 and white_sheet_y2 == black_sheet_1_y2:
        print("NO")
    elif black_sheet_1_x1 > white_sheet_x2 or black_sheet_1_x2 < white_sheet_x1 or black_sheet_1_y1 > white_sheet_y2 or black_sheet_1_y2 < white_sheet_y1:
        print("YES")
    elif black_sheet_2_x1 > white_sheet_x2 or black_sheet_2_x2 < white_sheet_x1 or black_sheet_2_y1 > white_sheet_y2 or black_sheet_2_y2 < white_sheet_y1:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()