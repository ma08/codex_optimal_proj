

def main():
    n = int(input())  # read input 
    s = input()  # read input

    if s.count('a') % 2 == 1:  # check if the string has an odd number of a's and b's
        print(1)
        print(s.replace('a', 'b', 1))
    elif s.count('b') % 2 == 1:  # check if the string has an odd number of a's and b's
        print(1)
        print(s.replace('b', 'a', 1))
    else:  # check if the string has an odd number of a's and b's
        print(0)
        print(s)

if __name__ == '__main__':
    main()
