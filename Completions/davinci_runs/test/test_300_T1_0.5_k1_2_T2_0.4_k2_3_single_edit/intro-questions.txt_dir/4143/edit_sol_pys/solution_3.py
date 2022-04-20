import math

N = int(input())
A, B, C, D, E = [int(i) for i in input().split()]

def minute_needed(num_people):
    return math.ceil(num_people / A) + math.ceil(num_people / B) + math.ceil(num_people / C) + math.ceil(num_people / D) + math.ceil(num_people / E)

print(minute_needed(N))
