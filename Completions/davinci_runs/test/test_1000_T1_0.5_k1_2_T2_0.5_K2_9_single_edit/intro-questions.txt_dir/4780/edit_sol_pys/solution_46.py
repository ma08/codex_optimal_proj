
N1, N2 = (int(x) for x in input().split())
line1 = list(input())
line2 = list(input())
T = int(input())

def swap(line, i, j):
    if i >= len(line) or j >= len(line):
        return
    line[i], line[j] = line[j], line[i]

for _ in range(T):
    swap(line1, 0, 1)
    swap(line2, -1, -2)
    if len(line1) == 0 or len(line2) == 0:
        break
    if line1[0] > line2[-1]:
        swap(line1, 0, 1)
        swap(line2, -1, -2)
    elif line1[0] < line2[-1]:
        swap(line1, 0, 1)
        swap(line2, -1, -2)

print(line1 + line2)
