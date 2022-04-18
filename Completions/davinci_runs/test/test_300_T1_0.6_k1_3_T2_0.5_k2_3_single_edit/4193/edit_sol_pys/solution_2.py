

# --- My answer ---
def bingo(sheet, bingo_nums):
    sheet_set = set(sheet)
    if len(sheet_set) < 3 or bingo_nums.count(0) < 3:
        return False
    else:
        for row in sheet:
            if len(set(row)) == 1:
                return True
        for i in range(3):
            if len(set([row[i] for row in sheet])) == 1:
                return True
        if len(set([sheet[i][i] for i in range(3)])) == 1:
            return True
        if len(set([sheet[i][2-i] for i in range(3)])) == 1:
            return True
    return False

def main(input_list):
    sheet = [input_list[i:i+3] for i in range(0, 9, 3)] # 3x3のリストを作る
    bingo_nums = [int(input_list[i]) for i in range(9, len(input_list))] # bingoのリストを作る

    for b in bingo_nums:
        for i in range(3):
            if b in sheet[i]: # bingoのリストに含まれている値が3x3のリストに含まれているか確認
                sheet[i][sheet[i].index(b)] = 0 # 含まれていたら0に変換

    if bingo(sheet):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    input_list = input().split()
    main(input_list)

# --- Book answer ---
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
    sheet = [list(map(int, input_list[i:i+3])) for i in range(0, 9, 3)]
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
