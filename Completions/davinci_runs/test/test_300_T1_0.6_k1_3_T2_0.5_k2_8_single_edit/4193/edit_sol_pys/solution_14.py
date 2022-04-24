
import sys

# Read data
a = [list(map(int, line.split())) for line in sys.stdin.readlines()[:3]]
b = [int(line.rstrip()) for line in sys.stdin.readlines()[3:]]

# Check bingo (horizontal)
for i in range(3):
    if len(set(a[i]) & set(b)) == 3:
        print("Yes")
        sys.exit()

# Check bingo (vertical)
for j in range(3):
    if len(set([a[i][j] for i in range(3)]) & set(b)) == 3:
        print("Yes")
        sys.exit()

# Check bingo (diagonal)
if len(set([a[i][i] for i in range(3)]) & set(b)) == 3:
    print("Yes")
    sys.exit()
if len(set([a[i][2-i] for i in range(3)]) & set(b)) == 3:
    print("Yes")
    sys.exit()

# No bingo
print("No")
