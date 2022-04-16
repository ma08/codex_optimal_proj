

N1, N2 = (int(x) for x in input().split()) # 2 3
line1 = input() # abc
line2 = input() # def
T = int(input()) # 2

def swap(line, i):
    if i >= len(line):
        return line
    line = list(line)
    line[i], line[i+1] = line[i+1], line[i]
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
