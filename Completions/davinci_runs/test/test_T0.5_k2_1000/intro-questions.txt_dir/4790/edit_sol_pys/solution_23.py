

def main():
    string = input()  # input string
    black_count = 0
    white_count = 0
    for i in range(len(string)):  # count black and white
        if string[i] == 'B':
            black_count += 1
        else:
            white_count += 1
    if abs(black_count - white_count) > 1:  # if difference is more than 1
        print(0)
        return
    if black_count > white_count:  # if black is more than white
        target = 'B'
    else:  # if white is more than black
        target = 'W'
    if string[0] != target and string[-1] != target:
        print(0)
        return
    print(1)

main()
