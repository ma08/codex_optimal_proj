

def main():
    # read input
    X = int(input())
    queue = input().strip()

    # find the number of people we can let in the club
    num_men = 0
    num_women = 0
    num_people = 0
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
