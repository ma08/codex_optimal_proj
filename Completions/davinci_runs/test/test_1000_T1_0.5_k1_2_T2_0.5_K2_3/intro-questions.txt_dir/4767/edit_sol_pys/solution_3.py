
import sys


def main():
    vals = [int(x) for x in sys.stdin.readline().split()]  # list of scores
    out = 0  # initialise out
    for i in range(8):  # for each score
        out += 19 - vals[i]  # add 19 - score to out
    print(out)  # print out


main()
