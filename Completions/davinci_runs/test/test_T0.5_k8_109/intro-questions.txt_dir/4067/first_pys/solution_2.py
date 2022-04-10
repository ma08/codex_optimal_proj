

def balanced_ternary_string(s):
    s_dict = {'0': 0, '1': 0, '2': 0}
    for c in s:
        s_dict[c] += 1

    if s_dict['0'] == s_dict['1'] and s_dict['1'] == s_dict['2']:
        return s

    # If the difference between the number of 0s and 1s is more than 1, we need to change some 0s to 1s
    if abs(s_dict['0'] - s_dict['1']) > 1:
        if s_dict['0'] > s_dict['1']:
            s = s.replace('0', '1', 1)
        else:
            s = s.replace('1', '0', 1)

    # If the difference between the number of 1s and 2s is more than 1, we need to change some 1s to 2s
    if abs(s_dict['1'] - s_dict['2']) > 1:
        if s_dict['1'] > s_dict['2']:
            s = s.replace('1', '2', 1)
        else:
            s = s.replace('2', '1', 1)

    # If the difference between the number of 0s and 1s is more than 1, we need to change some 0s to 1s
    if abs(s_dict['0'] - s_dict['1']) > 1:
        if s_dict['0'] > s_dict['1']:
            s = s.replace('0', '1', 1)
        else:
            s = s.replace('1', '0', 1)

    return s

if __name__ == "__main__":
    s = input()
    print(balanced_ternary_string(s))