

from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, x, y = [int(x) for x in stdin.readline().strip().split()]
    if n == 2:
        stdout.write(str(x) + " " + str(y) + "\n")
    elif n == 3:
        stdout.write(str(x) + " " + str(y) + " " + str(x+y) + "\n")
    elif n == 4:
        stdout.write(str(x) + " " + str(y) + " " + str(x+y) + " " + str(x*y) + "\n")
    else:
        if n % 2 == 0:
            stdout.write(str(x) + " " + str(y) + " " + str(x+y) + " " + str((n-4)//2*x*y) + " " + str(x*y) + " " + str(x+y) + " " + str((n-4)//2*x*y) + " " + str(x*y) + "\n")
        else:
            stdout.write(str(x) + " " + str(y) + " " + str(x+y) + " " + str((n-5)//2*x*y) + " " + str(x*y) + " " + str(x+y) + " " + str((n-5)//2*x*y) + " " + str(x*y) + " " + str(x) + "\n")
