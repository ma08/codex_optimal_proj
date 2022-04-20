
N = int(input())
A = [int(i) for i in input().split()]

def minute_needed(num_people):
    return (num_people + A[0] - 1) // A[0] + (num_people + A[1] - 1) // A[1] + (num_people + A[2] - 1) // A[2] + (num_people + A[3] - 1) // A[3] + (num_people + A[4] - 1) // A[4]

print(minute_needed(N))
