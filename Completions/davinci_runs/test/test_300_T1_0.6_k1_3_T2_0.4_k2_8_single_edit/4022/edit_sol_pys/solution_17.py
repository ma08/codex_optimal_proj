

from random import randint
import sys

def test_data():
    """ Generates a test case with n segments. """

    n = 3
    # n = randint(2, 3 * 10 ** 5)
    segments = [[randint(0, 10 ** 9), randint(0, 10 ** 9)] for _ in range(n)]
    segments.sort()
    return n, segments

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
        return 0

    # Find the middle and the highest segment.
    middle = (n - 1) // 2
    maximum = max(segments[middle][1], segments[middle + 1][1])

    # Remove the segment with the highest right endpoint.
    if segments[middle][1] == maximum:
        return max(
            solution(n - 1, segments[:middle] + segments[middle + 1:]),
            min(segments[middle][1], segments[middle - 1][1]) - max(segments[middle][0], segments[middle - 1][0])
        )
    else:
        return max(
            solution(n - 1, segments[:middle + 1] + segments[middle + 2:]),
            min(segments[middle][1], segments[middle + 1][1]) - max(segments[middle][0], segments[middle + 1][0])
        )

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, segments = next(reader)
    segments = list(reader)
    segments.sort()
    print(solution(n, segments))

if __name__ == "__main__":
    main()
