
import sys

def main():
    # read the input and convert to an int
    n = int(sys.stdin.readline())

    # read the input and convert to a list of strings
    l = sys.stdin.readline().split()
    #print(l)

    # convert the list of strings to a list of ints
    l = list(map(int, l))
    #print(l)

    # find the min, max, and average of the list
    min = min(l)
    max = max(l)
    avg = sum(l) / len(l)
    #print(min, max, avg)

    # print the min, max, and average
    print(min, max, avg)

    return 0

if __name__ == "__main__":
    main()
