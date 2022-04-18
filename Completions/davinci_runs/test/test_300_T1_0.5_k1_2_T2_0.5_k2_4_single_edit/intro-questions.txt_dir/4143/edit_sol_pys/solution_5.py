
N = int(input())
A, B, C, D, E = [int(i) for i in input().split()]


def minute_needed(num_people, a, b, c, d, e):
    return (num_people + a - 1) // a + (num_people + b - 1) // b + (num_people + c - 1) // c + (num_people + d - 1) // d + (num_people + e - 1) // e


print(minute_needed(N))
