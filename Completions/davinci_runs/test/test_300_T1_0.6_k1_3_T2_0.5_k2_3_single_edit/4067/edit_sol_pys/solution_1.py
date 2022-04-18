
def main():
    n = int(input())
    s = input()

    zeros = [i for i, x in enumerate(s) if x == '0']
    ones = [i for i, x in enumerate(s) if x == '1']
    twos = [i for i, x in enumerate(s) if x == '2']
    if len(zeros) == len(ones) == len(twos):
        return s

    if len(zeros) > len(ones):
        s = s[:zeros[0]] + '1' + s[zeros[0]+1:]
        s = s[:ones[0]] + '0' + s[ones[0]+1:]
        return s[:zeros[1]] + '1' + s[zeros[1]+1:]
    else:
        s = s[:ones[0]] + '0' + s[ones[0]+1:]
        s = s[:zeros[0]] + '1' + s[zeros[0]+1:]
        return s[:ones[1]] + '0' + s[ones[1]+1:]


if __name__ == '__main__':
    print(main())
