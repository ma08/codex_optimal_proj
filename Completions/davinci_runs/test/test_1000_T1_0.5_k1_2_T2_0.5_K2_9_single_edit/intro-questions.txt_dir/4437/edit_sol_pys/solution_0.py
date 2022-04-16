

def main():
    # read input and convert to int
    n = int(input().strip())
    s = input().strip()

    # check if the string has an odd number of a's
    if s.count('a') % 2 == 1: print(1); print(s.replace('a', 'b', 1))
    # check if the string has an odd number of b's
    elif s.count('b') % 2 == 1: print(1); print(s.replace('b', 'a', 1))
    # otherwise the string is already balanced
    else: print(0); print(s)

if __name__ == '__main__':
    main()
