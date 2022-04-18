

N1, N2 = (int(x) for x in input().split())  # read the number of elements in each list
line1 = input()  # read the first line
line2 = input()  # read the second line
T = int(input())  # read the number of swaps


def swap(line, i):  # swap two elements in a list
    if i >= len(line):
        return line
    line = list(line)
    line[i], line[i + 1] = line[i + 1], line[i]
    return ''.join(line)

for _ in range(T):  # perform swaps
    line1 = swap(line1, 0)
    line2 = swap(line2, -1)
    if len(line1) == 0 or len(line2) == 0:  # if one of the lines is empty, stop
        break
    if line1[0] > line2[-1]:  # if the first element of line 1 is greater than the last element of line 2
        line1 = swap(line1, 0)
        line2 = swap(line2, -1)
    elif line1[0] < line2[-1]:  # if the first element of line 1 is less than the last element of line 2
        line1 = swap(line1, 1)
        line2 = swap(line2, -2)

print(line1 + line2)  # print the result
