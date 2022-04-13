
def swap(line, i):
    if i >= len(line):
        return line
    line = list(line)
    line[i], line[i+1] = line[i+1], line[i]

N1, N2 = (int(x) for x in input().split()) # length of each line
line1 = input() # first line
line2 = input() # second line
T = int(input())
    return ''.join(line)

for _ in range(T):
    line1 = swap(line1, 0)
    line2 = swap(line2, -1)
    if len(line1) == 0 or len(line2) == 0:
        break
    if line1[0] > line2[-1]:
        line1 = swap(line1, 0)
        line2 = swap(line2, -1)
    elif line1[0] < line2[-1]:
        line1 = swap(line1, 1)
        line2 = swap(line2, -2)

print(line1 + line2)
