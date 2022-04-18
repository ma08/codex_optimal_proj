import sys

s, v1, v2 = map(int, sys.stdin.readline().split())

# if s is divisible by v1, then we can just use s//v1 v1 bottles
if s % v1 == 0:
    print(s // v1, 0)
    sys.exit(0)

# if s is not divisible by v1, then we will need to use some v2 bottles to make up the difference
v1_bottles = s // v1
v2_bottles = 0

# if v1_bottles * v1 + v2_bottles * v2 >= s, then we are done
while v1_bottles * v1 + v2_bottles * v2 < s:
    # if we have used all v1 bottles, but still not enough v2 bottles, then we cannot meet the requirements
    if v1_bottles == 0:
        print("Impossible")
        sys.exit(0)
    # remove one v1 bottle, and add one v2 bottle
    v1_bottles -= 1
    v2_bottles += 1

print(v1_bottles, v2_bottles)
