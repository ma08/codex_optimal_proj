
import sys
def main():
    # read input
    X = int(sys.stdin.readline())
    queue = sys.stdin.readline()

    # find the number of people we can let in
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
    sys.stdout.write(str(num_people) + '\n')

if __name__ == "__main__":
    main()
