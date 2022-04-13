import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        test = test.split()
        n = int(test[0])
        shuffle = test[1].lower()
        if shuffle == "out":  # "out" means the card is facing down
            if n % 2 == 0:
                print(n // 2)
            else:
                print((n-1) // 2)
        else:  # "in" means the card is facing up
            if n % 2 == 0:
                print(n // 2)
            else:
                print(n // 2 + 1)
    test_cases.close()

if __name__ == '__main__':
    main()
