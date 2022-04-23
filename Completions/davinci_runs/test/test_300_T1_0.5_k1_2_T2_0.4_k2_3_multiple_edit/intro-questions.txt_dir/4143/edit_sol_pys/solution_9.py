N = int(input())
A, B, C, D, E = [int(i) for i in input().split()]

def minutes_needed(num_people):
    return (num_people + A - 1) // A + (num_people + B - 1) // B + (num_people + C - 1) // C + (num_people + D - 1) // D + (num_people + E - 1) // E - 5

print(minutes_needed(N))
