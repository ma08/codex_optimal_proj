

import sys

def main():
    aggr, calm, aggr2, calm2 = [int(n) for n in sys.stdin.readline().split()]  # noqa
    p, m, g = [int(n) for n in sys.stdin.readline().split()]
    if (p - 1) % (aggr + calm) < aggr and (p - 1) % (aggr2 + calm2) < aggr2:  # noqa
        print("both")
    elif (p - 1) % (aggr + calm) < aggr or (p - 1) % (aggr2 + calm2) < aggr2:  # noqa
        print("one")
    else:
        print("none")
    if (m - 1) % (aggr + calm) < aggr and (m - 1) % (aggr2 + calm2) < aggr2:  # noqa
        print("both")
    elif (m - 1) % (aggr + calm) < aggr or (m - 1) % (aggr2 + calm2) < aggr2:  # noqa
        print("one")
    else:
        print("none")
    if (g - 1) % (aggr + calm) < aggr and (g - 1) % (aggr2 + calm2) < aggr2:  # noqa
        print("both")
    elif (g - 1) % (aggr + calm) < aggr or (g - 1) % (aggr2 + calm2) < aggr2:  # noqa
        print("one")
    else:
        print("none")

main()
