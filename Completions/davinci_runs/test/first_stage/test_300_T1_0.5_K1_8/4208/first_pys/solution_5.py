

n = int(input())
l = input()
r = input()

def get_index(char):
    if char == '?':
        return -1
    else:
        return ord(char) - ord('a')

def solve():
    l_indexes = list(map(get_index, l))
    r_indexes = list(map(get_index, r))
    left_counts = [0] * 26
    right_counts = [0] * 26
    for index in l_indexes:
        if index >= 0:
            left_counts[index] += 1
    for index in r_indexes:
        if index >= 0:
            right_counts[index] += 1
    left_index = 0
    right_index = 0
    solutions = []
    while left_index < n and right_index < n:
        if l_indexes[left_index] == r_indexes[right_index]:
            solutions.append((left_index + 1, right_index + 1))
            left_index += 1
            right_index += 1
        elif l_indexes[left_index] < 0:
            left_index += 1
        elif r_indexes[right_index] < 0:
            right_index += 1
        elif left_counts[l_indexes[left_index]] <= right_counts[l_indexes[left_index]]:
            left_index += 1
        else:
            right_index += 1
    print(len(solutions))
    for solution in solutions:
        print(*solution)

solve()