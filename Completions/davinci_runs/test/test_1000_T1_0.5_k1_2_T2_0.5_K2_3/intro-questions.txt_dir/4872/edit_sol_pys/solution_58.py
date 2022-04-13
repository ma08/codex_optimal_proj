

n = int(input())
dirt = [int(x) for x in input().split()]

clean = 0
dirty = 0

for day in dirt:
    dirty += day 
    if dirty >= 20:
        clean += 1
        dirty = 0

print(clean)
