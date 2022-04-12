
import heapq

def solve(input):
    n = int(input[0])
    intervals = [list(map(int, line.split())) for line in input[1:n]]
    intervals.sort(key=lambda x: x[1])
    q = []
    count = 0
    for interval in intervals:
        if len(q) == 0 or q[0] < interval[0]:
            heapq.heappush(q, interval[1])
            count += 1
        else:
            heapq.heappop(q)
            heapq.heappush(q, interval[1])
    return count

if __name__ == '__main__':
    input = [
        '4',
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
