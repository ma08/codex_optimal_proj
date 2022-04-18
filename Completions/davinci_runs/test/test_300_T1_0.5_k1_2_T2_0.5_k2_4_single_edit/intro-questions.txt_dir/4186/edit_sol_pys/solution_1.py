

from sys import stdin


def main():
    n, k = [int(x) for x in stdin.readline().split()]

    # create a list of tuples of each number and the number of times it
    # occurs
    num_counts = []
    for i in range(1, k + 1):
        num_counts.append((i, n.count(i)))

    # sort the number counts by the number of times they occur
    num_counts.sort(key=lambda x: x[1])

    # find the minimum number of numbers needed to make a list of
    # length k
    min_nums = 0
    for i, count in num_counts:
        min_nums += count


    print(min_nums)

main()
