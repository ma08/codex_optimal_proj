

def get_min_difference(input_string):
    min_difference = 1001
    for i in range(len(input_string) - 2):
        difference = abs(753 - int(input_string[i:i+3]))
        if difference < min_difference:
            min_difference = difference
    return min_difference


if __name__ == '__main__':
    input_string = input()
    print(get_min_difference(input_string))
