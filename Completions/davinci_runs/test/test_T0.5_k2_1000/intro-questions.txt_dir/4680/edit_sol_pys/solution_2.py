import sys

a, b, c = map(int, sys.stdin.readline().split()) #read 3 integers from stdin

if a == 5 and b == 7 and c == 5: #check if they are equal to 5, 7 and 5
    print("YES")
else:
    print("NO")
