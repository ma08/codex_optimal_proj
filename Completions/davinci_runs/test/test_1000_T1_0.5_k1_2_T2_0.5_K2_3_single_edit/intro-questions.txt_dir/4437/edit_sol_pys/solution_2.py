

def main():
    # read input
    n = int(input())
    s = input()

    # check if the string has an odd number of a's and b's
    if s.count('a') % 2 == 1 and s.count('b') % 2 == 1:
        print(2)
        print(s.replace('a', 'b', 1), s.replace('b', 'a', 1))
    elif s.count('a') % 2 == 1:
        print(1)
        print(s.replace('a', 'b', 1))
    elif s.count('b') % 2 == 1 and s.count('a') % 2 == 1:
        print(2)
        print(s.replace('a', 'b', 1), s.replace('b', 'a', 1))
    elif s.count('b') % 2 == 1 and s.count('a') % 2 == 0:
        print(1)
        print(s.replace('b', 'a', 1))
    else:
        print(0)
        print(s)

if __name__ == '__main__':
    main()
