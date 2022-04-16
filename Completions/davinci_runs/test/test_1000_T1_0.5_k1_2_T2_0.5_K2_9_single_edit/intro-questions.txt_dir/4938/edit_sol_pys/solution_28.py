

def main():
    # read input
    X = int(input())  # maximum difference between number of men and women
    queue = input()  # queue of men and women

    # check input
    assert(len(queue) <= 100000)
    assert(X >= 0)
    for person in queue:
        assert(person in ['M', 'W'])

    # find the number of people we can let in
    num_men = 0
    num_women = 0
    num_people = 0  # number of people we can let in
    for person in queue:
        if person == 'M':
            num_men += 1
        else:
            num_women += 1
        if abs(num_men - num_women) > X:
            break
        num_people += 1

    # output result
    print(num_people)


if __name__ == "__main__":
    main()
