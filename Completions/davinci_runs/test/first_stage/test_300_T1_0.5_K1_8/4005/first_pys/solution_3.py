

def main():
    """
    1. read input
    2. check if white sheet is fully covered
    3. check if any point of white sheet lies outside of black sheets
    """
    white_sheet = [int(x) for x in input().split()]
    black_sheet_1 = [int(x) for x in input().split()]
    black_sheet_2 = [int(x) for x in input().split()]

    def check_if_fully_covered(white_sheet, black_sheet):
        if white_sheet[0] >= black_sheet[0] and \
           white_sheet[1] >= black_sheet[1] and \
           white_sheet[2] <= black_sheet[2] and \
           white_sheet[3] <= black_sheet[3]:
            return True
        else:
            return False

    def check_if_partially_covered(white_sheet, black_sheet):
        if white_sheet[0] < black_sheet[0] and \
           white_sheet[1] < black_sheet[1] and \
           white_sheet[2] > black_sheet[2] and \
           white_sheet[3] > black_sheet[3]:
            return True
        else:
            return False

    if check_if_fully_covered(white_sheet, black_sheet_1) and \
       check_if_fully_covered(white_sheet, black_sheet_2):
        print("NO")
        return
    elif check_if_partially_covered(white_sheet, black_sheet_1) or \
         check_if_partially_covered(white_sheet, black_sheet_2):
        print("YES")
        return
    else:
        print("NO")
        return

if __name__ == '__main__':
    main()