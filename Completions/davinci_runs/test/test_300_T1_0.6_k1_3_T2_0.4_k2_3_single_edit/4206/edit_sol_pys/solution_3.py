

def sum_digits_divisible_by_3(n):
    return sum(map(int, str(n))) % 3 == 0

def find_cuts(s):
    cuts = []
    i = 0
    while i < len(s) - 1:
        if not sum_digits_divisible_by_3(s[:i+1]):
            cuts.append(i + 1)
            i += 1
            continue
        i += 1
    if sum_digits_divisible_by_3(s[:i+1]):
        return cuts
    else:
        return cuts + [len(s)]

def get_sub_strings(s, cuts):
    sub_strings = []
    i = 0
    for cut in cuts:
        sub_strings.append(s[i:cut])
        i = cut
    sub_strings.append(s[i:])
    return sub_strings

def main():
    s = input()
    cuts = find_cuts(s)
    sub_strings = get_sub_strings(s, cuts)
    count = 0
    for sub_string in sub_strings:
        if sum_digits_divisible_by_3(sub_string):
            count += 1
    print(count)

if __name__ == '__main__':
    main()
