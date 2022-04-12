import heapq

def solve(input):
    n = int(input[0])
    intervals = [[int(x) for x in line.split()] for line in input[1:]]
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
    input = [
        '6',
        '1 4',
        '3 5',
        '0 6',
        '5 7',
        '3 8',
        '5 9',
        '6 10',
        '8 11',
        '8 12',
        '2 13',
        '12 14'
    ]
    print(solve(input))
