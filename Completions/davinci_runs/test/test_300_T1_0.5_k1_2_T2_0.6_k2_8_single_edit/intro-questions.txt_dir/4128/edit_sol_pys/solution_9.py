

import math
t = int(input()) #number of test cases


for i in range(t):
    n = int(input()) #number of elements
    arr = list(map(int, input().split())) #list of elements
    print(math.ceil(sum(arr)/n))
