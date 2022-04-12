N = int(input())
A, B, C, D, E = [int(i) for i in input().split()]


def minute_needed(num_people, A):
    return (num_people + A - 1) // A


print(minute_needed(N))
