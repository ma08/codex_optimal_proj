

# --- My answer ---
def bingo(sheet, nums):
    for i in range(3):
        if sum(sheet[i]) == 0:
            return True
        if sum([sheet[0][i], sheet[1][i], sheet[2][i]]) == 0:
            return True
    if sum([sheet[0][0], sheet[1][1], sheet[2][2]]) == 0:
        return True
    if sum([sheet[0][2], sheet[1][1], sheet[2][0]]) == 0:
        return True
    return False

def main(input_list):
    sheet = [list(map(int, input_list[i:i+3])) for i in range(0, 9, 3)] # [0:3], [3:6], [6:9]
    nums = list(map(int, input_list[9:]))

    for num in nums:
        for i in range(3):
            if num in sheet[i]:
                sheet[i][sheet[i].index(num)] = 0
    if bingo(sheet, nums):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    input_list = input().split()
    main(input_list)
