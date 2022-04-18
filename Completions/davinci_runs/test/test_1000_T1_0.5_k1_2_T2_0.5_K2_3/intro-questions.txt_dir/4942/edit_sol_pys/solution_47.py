
import sys

def main():
    num_segments = int(sys.stdin.readline().strip())
    segment_lengths = [int(x) for x in sys.stdin.readline().strip().split()]
    segment_lengths.sort()
    max_time = segment_lengths[-1]
    for i in range(len(segment_lengths) - 2, -1, -1):
        max_time += 1 + segment_lengths[i]
    print(max_time)

if __name__ == '__main__':
    main()
