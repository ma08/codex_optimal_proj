

def bingo(sheet):
    sheet_set = set(sheet)
    if len(sheet_set) < 3:
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

def main():
    sheet = [list(map(int, input().split())) for _ in range(3)]
    bingo_nums = list(map(int, input().split()))

    for b in bingo_nums:
        for i in range(3):
            if b in sheet[i]:
                sheet[i][sheet[i].index(b)] = 0

        if bingo(sheet):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    input_list = input().split()
    main()

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

def main():
    sheet = [list(map(int, input().split())) for _ in range(3)]
    nums = list(map(int, input().split()))

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
