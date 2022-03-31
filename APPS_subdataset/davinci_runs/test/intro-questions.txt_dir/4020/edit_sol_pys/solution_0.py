
import sys

def main():
    # get the input from the user
    h1, m1 = sys.stdin.readline().strip().split(":")
    h2, m2 = sys.stdin.readline().strip().split(":")
    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int(m2)
    # calculate the midpoint
    h = (h1 + h2) // 2
    m = (m1 + m2) // 2
    # check if we need to add an hour to the midpoint time
    if m > 59:
        h += 1
        m -= 60
    # check if we need to add a day to the midpoint
    if h > 23:
        h -= 24
    # print the result
    print("{:02d}:{:02d}".format(h, m))

if __name__ == "__main__":
    main()
