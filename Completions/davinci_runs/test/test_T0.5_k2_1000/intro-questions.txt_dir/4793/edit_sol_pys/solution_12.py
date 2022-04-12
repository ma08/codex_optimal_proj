
#------------------------------------------------------------------------------

import sys

#------------------------------------------------------------------------------

def main():
    """
    Main program.
    """
    # Read the input
    s, v1, v2 = [int(x) for x in sys.stdin.read().split()]

    # If the smaller bottle can't hold anything, then there is no solution
    if v2 == 0:
        print("Impossible")
        return

    # If the larger bottle is smaller than the shipment, then there is no solution.
    if v1 < s:
        print("Impossible")
        return

        return

    # If the larger bottle is the same size as the shipment, then we only need one bottle.
    if v1 == s:
        print("1 0")
        return

        return

    # If the smaller bottle is bigger than the shipment, then we need to use the smaller bottle.
    if v2 >= s:
        print("0 {}".format(s//v2))
        return

    # If we get here, then we have to use both bottles. We'll start by filling the larger bottle.
    large_bottles = s // v1
    small_bottles = 0
    remaining = s - large_bottles * v1

    # Now we'll fill the smaller bottles with whatever is left.
    small_bottles = remaining // v2

    remaining = remaining - small_bottles * v2

    # If there is still some left over, we need to add another large bottle.
    if remaining > 0:
        large_bottles += 1

    # Print the result
    print("{} {}".format(large_bottles, small_bottles))

#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
