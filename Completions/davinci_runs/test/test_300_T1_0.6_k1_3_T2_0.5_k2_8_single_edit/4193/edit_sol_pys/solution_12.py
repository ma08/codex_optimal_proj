

# --- My answer ---
def bingo(sheet):
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
    sheet = [input_list[i:i+3] for i in range(0, 9, 3)]
    bingo_nums = [int(input_list[i]) for i in range(9, len(input_list))]

    for b in bingo_nums:
        for i in range(3):
            if b in sheet[i]:
                sheet[i][sheet[i].index(b)] = 0

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
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    input_list = input().split()
    main(input_list)
