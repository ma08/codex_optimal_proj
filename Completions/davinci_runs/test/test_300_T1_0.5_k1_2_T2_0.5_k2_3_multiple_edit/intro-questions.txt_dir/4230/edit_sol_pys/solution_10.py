

import sys

def find_closest_segment(x, p):
    p.sort()

    if x < p[0]:
        return p[0] - x
    elif x > p[len(p)-1]:
        return x - p[len(p)-1]
    else:
        for i in range(1, len(p)):
            if p[i-1] < x and x < p[i]:
                if abs(p[i-1] - x) < abs(p[i] - x):
                    return p[i-1] - x
                else:
                    return p[i] - x
                break


def main():
    x = int(input())  # the position of the center of the segment
    n = int(input())
    p = list(map(int, input().split()))  # the positions of the centers of the segments

    print(find_closest_segment(x, p))


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        print(find_closest_segment(0, [7, 8, 9]))
        print(find_closest_segment(6, [4]))
        print(find_closest_segment(3, [1, 4, -3]))
        print(find_closest_segment(9, [1, 4, -3]))
        print(find_closest_segment(0, [1, 4, -3]))
        print(find_closest_segment(1, [1, 4, -3]))
        print(find_closest_segment(2, [1, 4, -3]))
        print(find_closest_segment(3, [1, 4, -3]))
        print(find_closest_segment(4, [1, 4, -3]))
        print(find_closest_segment(5, [1, 4, -3]))
        print(find_closest_segment(6, [1, 4, -3]))
        print(find_closest_segment(7, [1, 4, -3]))
        print(find_closest_segment(8, [1, 4, -3]))
        print(find_closest_segment(9, [1, 4, -3]))
        print(find_closest_segment(10, [1, 4, -3]))

        print(find_closest_segment(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(6, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(7, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(8, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(9, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(13, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(14, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(15, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(17, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(18, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(19, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        print(find_closest_segment(20,
            else:
                print(p[i] - x)
            break
