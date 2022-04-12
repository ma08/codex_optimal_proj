import sys

n, p = map(int, sys.stdin.readline().split())  # n = number of houses, p = number of people
distances = sorted(map(int, sys.stdin.readline().split()))  # distances of houses from the hospital

if p == 1:
    print(1)
else:
    i = 0  # index
    while i < n:  # while index is less than the number of houses
        if i + p - 1 < n:  # if index + number of people - 1 is less than the number of houses
            if distances[i] != distances[i + p - 1]:  # if the distance of the house at the index is not equal to the distance of the house at the index + number of people - 1
                print(distances[i + p - 1])  # print the distance of the house at the index + number of people - 1
                break  # break the while loop
        i += 1  # increment the index
