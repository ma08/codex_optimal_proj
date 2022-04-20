
import sys

def test_data():
    """ Generates a test case with n segments. """

    n = 3
    segments = [[random.randint(0, 10 ** 9), random.randint(0, 10 ** 9)] for _ in range(n)]
    segments.sort()
    return n, segments, solution(n, segments)

def solution(n, segments):
    """ Returns the maximum length of the intersection of n - 1 segments. """

    # If n == 2, return the length of the intersection of the two segments.
    if n == 2:
        return max(0, min(segments[1][1], segments[0][1]) - max(segments[0][0], segments[1][0]))

    # If the intersection of the first two segments is empty, return 0.
    if segments[0][1] < segments[1][0]:
        return 0

    # If the intersection of the last two segments is empty, return 0.
    if segments[-1][0] > segments[-2][1]:
    intersection = min(segments[middle][1], segments[middle + 1][1]) - max(segments[middle][0], segments[middle + 1][0])
        return 0

    # Find the middle and the highest segment, and the intersection of the middle two segments.
    middle = (n - 1) // 2
    maximum = max(segments[middle][1], segments[middle + 1][1])

    # Remove the segment with the highest right endpoint.
    if segments[middle][1] == maximum:
        return max(
            solution(n - 1, segments[:middle] + segments[middle + 1:]),
            intersection
        )
    else:
        return max(
            solution(n - 1, segments[:middle + 1] + segments[middle + 2:]),
            intersection
        )

def main():
    reader = (map(int, line.split()) for line in sys.stdin) # Reads in the input.
    n, segments = next(reader), list(reader) # Separates the number of segments and the segments.
    segments.sort()
    print(solution(n, segments))

if __name__ == "__main__":
    main()
