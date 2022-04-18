import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if test[0] == "0":
        print("1")
    elif test[0] == "1":
        print("66")
    elif test[0] == "2":
        print("56")
    elif test[0] == "3":
        print("96")
    elif test[0] == "4":
        print("36")
    elif test[0] == "5":
        print("76")
    elif test[0] == "6":
        print("16")
    elif test[0] == "7":
        print("56")
    elif test[0] == "8":
        print("96")
    elif test[0] == "9":
        print("36")
test_cases.close()
