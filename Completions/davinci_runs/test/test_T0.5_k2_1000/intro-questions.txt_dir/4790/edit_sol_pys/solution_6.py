

def main():
    string = input()
    black_count = 0
    white_count = 0
    for i in range(len(string)):
        if string[i] == 'B':
            black_count += 1
        else:
            white_count += 1
    if abs(black_count - white_count) > 1:
        # if the number of black and white is more than 1, there is no possible way to make it valid
        print(0)
        return
    if black_count == white_count:
        # if the number of black and white is the same, it is always valid
        print(1)
        return
    if black_count > white_count:
        target = 'B'
    else:
        target = 'W'
    for i in range(len(string)):
        if string[i] == target:
            if i == 0:
                if string[-1] != target and string[1] != target:
                    print(0)
                    return
            elif i == len(string) - 1:
                if string[-2] != target and string[0] != target:
                    print(0)
                    return
            else:
                if string[i-1] != target and string[i+1] != target:
                    print(0)
                    return
    print(1)

main()
