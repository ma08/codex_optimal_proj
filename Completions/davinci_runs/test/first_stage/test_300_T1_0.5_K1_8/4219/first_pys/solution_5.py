

# Read input
n = int(input())
people = [0 for _ in range(n)]
for i in range(n):
    testimonies = []
    for _ in range(int(input())):
        testimonies.append(list(map(int, input().split())))
    people[i] = testimonies

# Find the maximum number of honest people
max_honest_people = 0
for i in range(1, 2**n):
    # Binary representation of i
    binary_i = bin(i)[2:].zfill(n)

    # Test if the combination of honest people is valid
    valid = True
    for j in range(n):
        if binary_i[j] == '1':
            for k in range(len(people[j])):
                if binary_i[people[j][k][0]-1] != str(people[j][k][1]):
                    valid = False
                    break
        if not valid:
            break
    if valid:
        max_honest_people = max(max_honest_people, binary_i.count('1'))

# Print the result
print(max_honest_people)