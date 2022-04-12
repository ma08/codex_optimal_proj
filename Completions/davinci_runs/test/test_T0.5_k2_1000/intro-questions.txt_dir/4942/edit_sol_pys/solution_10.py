
import sys
import heapq

def party_planning(trees):
    """
    The party can be organized at the earliest on the next day after the last tree has grown up.
    :param trees: list of ints representing the number of days it takes for each tree to grow
    :return: earliest day when the party can be organized
    """
    # sort the list of trees by growth time
    heapq.heapify(trees)
    # the first tree takes 1 day to plant
    cur_day = 1
    # the earliest day that the party can be organized is the next day after the last tree has grown up
    # so we need to keep track of the last day that a tree will finish growing
    last_day = 0
    while trees:
        # plant the tree with the shortest growth time
        cur_day += heapq.heappop(trees)
        # if the current tree finishes growing after the previous tree, then the party can be organized
        # on the same day as the current tree
        if cur_day > last_day:
            last_day = cur_day
    return last_day

def main():
    """
    Driver function
    """
    trees = []
    for line in sys.stdin:
        trees.extend(map(int, line.split()))
    print(party_planning(trees))

if __name__ == "__main__":
    main()
