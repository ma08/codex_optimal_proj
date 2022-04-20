

n, x, y = [int(x) for x in input().split()]  # Read the input
s = input()  # Read the input

if int(s[x-y:x]) == 0:  # Check if the number is zero
    print(1)
else:
    print(0)
