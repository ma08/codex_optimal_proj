
import sys

def main():
    aggr, calm, aggr2, calm2 = [int(n) for n in sys.stdin.readline().split()]
    p, m, g = [int(n) for n in sys.stdin.readline().split()]
    for n in [p, m, g]:
        if (n - 1) % (aggr + calm) < aggr and (n - 1) % (aggr2 + calm2) < aggr2:
            print("both")
        elif (n - 1) % (aggr + calm) < aggr or (n - 1) % (aggr2 + calm2) < aggr2:
            print("one")
        else:
            print("none")

main()
