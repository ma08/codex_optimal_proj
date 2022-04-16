

import heapq

def solve(input):
    n = int(input[0])
    intervals = [list(map(int, line.split())) for line in input[1:]]  # list of lists
    intervals.sort(key=lambda x: x[1])
    q = []  # min heap
    for interval in intervals:
        if len(q) == 0 or q[0] > interval[0]:  # if q is empty or the first element in q is greater than the start of the current interval
            heapq.heappush(q, interval[1])
        else:
            heapq.heappop(q)
            heapq.heappush(q, interval[1])
    return len(q)  # number of elements in q is the maximum number of overlapping intervals


if __name__ == '__main__':
    input = [
        '3',
        '1 2',
        '2 4',
        '5 6'
    ]
    print(solve(input))
