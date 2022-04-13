
import heapq

def solve(input):
    intervals = [list(map(int, line.split())) for line in input[1:]]
    intervals.sort(key=lambda x: x[1])
    q = []
    for interval in intervals:
        if len(q) == 0 or q[0] > interval[0]:
            heapq.heappush(q, interval[1])
        else:
            heapq.heappop(q)
            heapq.heappush(q, interval[1])
    return len(q)


if __name__ == '__main__':
    input = ['3', '1 2', '2 4', '5 6']
    print(solve(input))
