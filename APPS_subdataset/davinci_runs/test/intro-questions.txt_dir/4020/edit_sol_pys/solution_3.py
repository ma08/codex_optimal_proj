
import sys

def main():
    # get the input from the user
    h1, m1 = sys.stdin.readline().strip().split(':') # get the first time
    h2, m2 = sys.stdin.readline().strip().split(':') # get the second time
    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int(m2)
    # calculate the midpoint
    h = (h1 + h2) // 2 # get the midpoint of the hours
    m = (m1 + m2) // 2 # get the midpoint of the minutes
    # check if we need to add an hour to the midpoint time
    if m > 59: # check if we need to add an hour to the midpoint time
        h += 1 # add an hour to the midpoint
        m -= 60 # subtract an hour from the midpoint
    # check if we need to add a day to the midpoint
    if h > 23: # check if we need to add a day to the midpoint
        h -= 24 # subtract a day from the midpoint
    # print the result
    print("{:02d}:{:02d}".format(h, m))

if __name__ == "__main__":
    main()
