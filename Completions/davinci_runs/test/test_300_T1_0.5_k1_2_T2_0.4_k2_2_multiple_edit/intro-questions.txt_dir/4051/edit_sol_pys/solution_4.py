
from collections import Counter
import sys

n = int(input())
arr = list(map(int, input().split())) #[1,2,3,4,5,6,7,8,9,10]

def count_triplets(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] < arr[j] < arr[k]:
                    count += 1
    return count

print(count_triplets(arr))
