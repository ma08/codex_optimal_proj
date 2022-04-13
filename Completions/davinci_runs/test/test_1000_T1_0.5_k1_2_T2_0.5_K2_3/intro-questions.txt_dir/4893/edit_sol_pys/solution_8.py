import sys

n, p = map(int, sys.stdin.readline().split())  # number of people, number of people in a group
distances = sorted(map(int, sys.stdin.readline().split()))  # list of distances

if p == 1:  # if there is only one person in a group, then print 1
    print(1)
else:  # otherwise, find the minimum distance
    i = 0
    while i < n:  # loop through distances
        if i + p - 1 < n:  # if the index of the last person in the group is less than the number of people
            if distances[i] != distances[i + p - 1]:  # if the first person's distance is not the same as the last person's distance
                print(distances[i + p - 1])  # print the last person's distance
                break
        i += 1  # increment index
