
import sys

def main():
    num_participants, budget, num_hotels, num_weeks = map(int, sys.stdin.readline().split()) # read in the first line
    for h in range(num_hotels):
        price = int(sys.stdin.readline()) # read in the price
        beds = map(int, sys.stdin.readline().split()) # read in the beds
        # check if there are enough beds for the participants and the price is within budget
        for w in range(num_weeks):
            if beds[w] >= num_participants and price * num_participants <= budget:
                print price * num_participants # print the price
                return # exit the program
    print "stay home" # if no hotel matches the criteria, print "stay home"

if __name__ == "__main__":
    main()
