
import sys

def main():
    aggr, calm, aggr2, calm2 = [int(n) for n in sys.stdin.readline().split()] # read in the values
    p, m, g = [int(n) for n in sys.stdin.readline().split()] # read in the values
    if (p - 1) % (aggr + calm) < aggr and (p - 1) % (aggr2 + calm2) < aggr2: # check if the first value is divisible by both
        print("both")
    elif (p - 1) % (aggr + calm) < aggr or (p - 1) % (aggr2 + calm2) < aggr2: # check if the first value is divisible by one
        print("one")
    else: # if the first value is not divisible by either
        print("none")
    if (m - 1) % (aggr + calm) < aggr and (m - 1) % (aggr2 + calm2) < aggr2: # check if the second value is divisible by both
        print("both")
    elif (m - 1) % (aggr + calm) < aggr or (m - 1) % (aggr2 + calm2) < aggr2: # check if the second value is divisible by one
        print("one")
    else: # if the second value is not divisible by either
        print("none")
    if (g - 1) % (aggr + calm) < aggr and (g - 1) % (aggr2 + calm2) < aggr2: # check if the third value is divisible by both
        print("both")
    elif (g - 1) % (aggr + calm) < aggr or (g - 1) % (aggr2 + calm2) < aggr2: # check if the third value is divisible by one
        print("one")
    else:
        print("none")

main()
