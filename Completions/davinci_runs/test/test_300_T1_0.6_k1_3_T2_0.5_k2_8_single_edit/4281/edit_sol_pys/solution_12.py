
import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))

    # Sort the input arrays
    a.sort()
    b.sort()
    c.sort()

    # Initialize the number of occupied houses
    num_houses = 0

    # Initialize the array of houses that are occupied by all three friends
    occupied_houses = []

    # Initialize the index of the first element of the array of houses
    # that are occupied by all three friends
    first = 0

    # Initialize the index of the last element of the array of houses
    # that are occupied by all three friends
    last = 0

    # Initialize the index of the first element of the array of houses
    # occupied by all three friends that are within the range of the
    # houses occupied by the first friend
    first1 = 0

    # Initialize the index of the last element of the array of houses
    # occupied by all three friends that are within the range of the
    # houses occupied by the first friend
    last1 = 0

    # Initialize the index of the first element of the array of houses
    # occupied by all three friends that are within the range of the
    # houses occupied by the second friend
    first2 = 0

    # Initialize the index of the last element of the array of houses
    # occupied by all three friends that are within the range of the
    # houses occupied by the second friend
    last2 = 0

    # Initialize the index of the first element of the array of houses
    # occupied by all three friends that are within the range of the
    # houses occupied by the third friend
    first3 = 0

    # Initialize the index of the last element of the array of houses
    # occupied by all three friends that are within the range of the
    # houses occupied by the third friend
    last3 = 0

    # Iterate over all houses occupied by the first friend
    for i in range(n):

        # Find the index of the first house occupied by the second friend
        # that is within the range of the houses occupied by the first friend
        while first2 < m and b[first2] < a[i]:
            first2 += 1

        # Find the index of the last house occupied by the second friend
        # that is within the range of the houses occupied by the first friend
        while last2 < m and b[last2] <= a[i]:
            last2 += 1

        # Find the index of the first house occupied by the third friend
        # that is within the range of the houses occupied by the first friend
        while first3 < m and c[first3] < a[i]:
            first3 += 1

        # Find the index of the last house occupied by the third friend
        # that is within the range of the houses occupied by the first friend
        while last3 < m and c[last3] <= a[i]:
            last3 += 1

        # Find the index of the first house occupied by all three friends
        # that is within the range of the houses occupied by the first friend
        while first < m and b[first] < a[i]:
            first += 1

        # Find the index of the last house occupied by all three friends
        # that is within the range of the houses occupied by the first friend
        while last < m and b[last] <= a[i]:
            last += 1

        # The number of houses occupied by all three friends that are within
        # the range of the houses occupied by the first friend is equal to
        # the number of houses occupied by the second and third friends that
        # are within the range of the houses occupied by the first friend
        occupied_houses.append(last2 - first2 + last3 - first3 - (last - first))

    # Iterate over all houses occupied by the second friend
    for i in range(m):

        # Find the index of the first house occupied by the first friend
        # that is within the range of the houses occupied by the second friend
        while first1 < n and a[first1] < b[i]:
            first1 += 1

        # Find the index of the last house occupied by the first friend
        # that is within the range of the houses occupied by the second friend
        while last1 < n and a[last1] <= b[i]:
            last1 += 1

        # The number of houses occupied by all three friends that are within
        # the range of the houses occupied by the second friend is equal to
        # the number of houses occupied by the first and third friends that
        # are within the range of the houses occupied by the second friend
        num_houses += last1 - first1 - occupied_houses[last1 - 1]

    # Print the number of houses occupied by all three friends
    print(num_houses)

if __name__ == "__main__":
    main()
