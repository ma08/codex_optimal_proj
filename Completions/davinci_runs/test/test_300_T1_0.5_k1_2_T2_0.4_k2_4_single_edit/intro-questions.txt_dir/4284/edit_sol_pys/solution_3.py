

import math

def max_turns(k, n, a, b): #k = number of keys, n = number of locks, a = number of keys per turn, b = number of locks per turn
    max_turns_1 = math.floor(k/a) #maximum number of turns of type 1
    max_turns_2 = math.floor(k/b) #maximum number of turns of type 2
    if max(max_turns_1, max_turns_2) < n: #if the maximum number of turns is less than n, then the answer is -1
        return -1 
    return max(max_turns_1, max_turns_2) #otherwise, the answer is the maximum number of turns

q = int(input()) #number of queries
for _ in range(q): 
    k, n, a, b = map(int, input().split()) #input k, n, a, b
    print(max_turns(k, n, a, b)) #output the maximum number of turns
