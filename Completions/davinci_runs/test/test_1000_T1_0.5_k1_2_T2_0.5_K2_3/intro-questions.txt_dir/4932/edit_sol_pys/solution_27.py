
import sys

def main():
    agg, calm, agg2, calm2 = [int(n) for n in sys.stdin.readline().split()]
    p, m, g = [int(n) for n in sys.stdin.readline().split()]
    if (p - 1) % (agg + calm) < agg and (p - 1) % (agg2 + calm2) < agg2:
        print("both")
    elif (p - 1) % (agg + calm) < agg or (p - 1) % (agg2 + calm2) < agg2:
        print("one")
    else:
        print("none")
    if (m - 1) % (agg + calm) < agg and (m - 1) % (agg2 + calm2) < agg2:
        print("both")
    elif (m - 1) % (agg + calm) < agg or (m - 1) % (agg2 + calm2) < agg2:
        print("one")
    else:
        print("none")
    if (g - 1) % (agg + calm) < agg and (g - 1) % (agg2 + calm2) < agg2:
        print("both")
    elif (g - 1) % (agg + calm) < agg or (g - 1) % (agg2 + calm2) < agg2:
        print("one")
    else:
        print("none")

main()
