

def main():
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            test = test.strip().split()
            if len(test) > 1:
                number = int(test[0])
                shuffle = test[1]
                count = 0
                if shuffle == 'out':
                    while number > 1:
                        number = int(number / 2)
                        count += 1
                else:
                    while number > 1:
                        number = int(number / 2)
                        count += 1
                    count = math.pow(2, count)
                print(int(count))


main()
