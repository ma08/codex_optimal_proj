
def swap(line, i):
    if i >= len(line) - 1:
        return line
    line = list(line)
    line[i], line[i+1] = line[i+1], line[i]
    return ''.join(line)

N1, N2 = [int(x) for x in input().split()]
line1 = list(input())
line2 = list(input())
T = int(input())

for _ in range(T):
    if len(line1) == 0 or len(line2) == 0 or line1[0] == line2[-1]:
        break

    if line1[0] > line2[-1]:
        line1 = swap(line1, 1)
        line2 = swap(line2, -2)
    elif line1[0] < line2[-1]:
        line1 = swap(line1, 0)
        line2 = swap(line2, -1)

print(''.join(line1 + line2))
