

import math
import os
import random
import re
import sys

def findMedian(arr):
    arr.sort()
    return arr[len(arr)//2]

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notifications = 0

    for i in range(len(expenditure)):
        if i >= d:
            median = findMedian(expenditure[i-d:i])
            if expenditure[i] >= 2*median:
                notifications += 1
    return notifications

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
