

def main():
    white_sheet = [int(x) for x in input().split()]
    black_sheet_1 = [int(x) for x in input().split()]
    black_sheet_2 = [int(x) for x in input().split()]

    # white sheet is fully covered by the black sheets
    if (white_sheet[0] >= black_sheet_1[0] and white_sheet[1] >= black_sheet_1[1] and white_sheet[2] <= black_sheet_1[2] and white_sheet[3] <= black_sheet_1[3]) or (white_sheet[0] >= black_sheet_2[0] and white_sheet[1] >= black_sheet_2[1] and white_sheet[2] <= black_sheet_2[2] and white_sheet[3] <= black_sheet_2[3]):
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    main()