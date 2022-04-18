

def check_bingo(bingo_card, numbers_called):

    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"

    # check horizontal
    for i in range(3):
        if bingo_card[i][0] in numbers_called and bingo_card[i][1] in numbers_called and bingo_card[i][2] in numbers_called:
            return 'Yes'

    # check vertical
    for i in range(3):
        if bingo_card[0][i] in numbers_called and bingo_card[1][i] in numbers_called and bingo_card[2][i] in numbers_called:
            return 'Yes'

    # check diagonal
    if bingo_card[0][0] in numbers_called and bingo_card[1][1] in numbers_called and bingo_card[2][2] in numbers_called:
        return 'Yes'
    if bingo_card[0][2] in numbers_called and bingo_card[1][1] in numbers_called and bingo_card[2][0] in numbers_called:
        return 'Yes'

    return 'No'


if __name__ == '__main__':
    bingo_card = []
    for i in range(3):
        bingo_card.append(list(map(int, input().split())))
    numbers_called = []
    for i in range(int(input())):
        numbers_called.append(int(input()))
    print(check_bingo(bingo_card, numbers_called))
