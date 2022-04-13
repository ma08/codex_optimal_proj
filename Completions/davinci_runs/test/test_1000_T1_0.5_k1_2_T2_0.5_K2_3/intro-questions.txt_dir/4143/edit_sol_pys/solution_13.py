
def minute_needed(num_people):
    return (num_people + A - 1) // A + (num_people + B - 1) // B + (num_people + C - 1) // C + (num_people + D - 1) // D + (num_people + E - 1) // E

N = int(input()) # number of people
A, B, C, D, E = [int(i) for i in input().split()] # number of people each bus can hold

print(minute_needed(N))
