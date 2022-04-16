

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
        return 0
    if black_count == white_count:
        return 1
    if black_count > white_count:
        target = 'B'
    else:
        target = 'W'
    for i in range(len(string)):
        if string[i] == target:
            if i == 0:
                if string[-1] != target and string[1] != target:
                    return 0
            elif i == len(string) - 1:
                if string[-2] != target and string[0] != target:
                    return 0
            else:
                if string[i-1] != target and string[i+1] != target:
                    return 0
    return 1

print(main())
