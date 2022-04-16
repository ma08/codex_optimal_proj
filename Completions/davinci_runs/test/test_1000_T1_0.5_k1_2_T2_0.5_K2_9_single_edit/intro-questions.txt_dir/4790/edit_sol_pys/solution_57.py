

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
        print(0)
        return
    if black_count > white_count:
        target = 'B'
    else:
        target = 'W'
    if string[0] == target:
        if string[-1] != target and string[1] != target:
            print(0)
            return
    elif string[-1] == target:
        if string[-2] != target and string[0] != target:
            print(0)
            return
    else:
        for i in range(len(string)):
            if string[i] == target:
                if string[i-1] != target and string[i+1] != target:
                    print(0)
                    return
    print(1)

main()
