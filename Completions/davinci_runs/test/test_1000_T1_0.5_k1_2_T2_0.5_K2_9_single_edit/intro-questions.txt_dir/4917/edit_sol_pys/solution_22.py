
import sys

def main():
    n = int(sys.stdin.readline().rstrip('\n')) 
    intervals = []
    for i in range(n):
        a, b = [int(x) for x in sys.stdin.readline().rstrip('\n').split()] 
        intervals.append([a, b])
    intervals.sort() 
    intervals_in_common = []
    for i in range(n-1): 
        start = max(intervals[i][0], intervals[i+1][0])
        end = min(intervals[i][1], intervals[i+1][1])
        if start <= end: 
            intervals_in_common.append([start, end])
    if len(intervals_in_common) == 0: 
        print("edward is right")
    else: 
        print("gunilla has a point")

if __name__ == '__main__':
    main()
