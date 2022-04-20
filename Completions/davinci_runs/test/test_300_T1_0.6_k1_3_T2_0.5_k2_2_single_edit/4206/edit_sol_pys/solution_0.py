import sys


input = sys.stdin.readline()

if len(input) == 1:
    sys.stdout.write(1)
else:
    count = 0
    for i in range(1, len(input)):
        if int(input[:i]) % 3 == 0:
            count += 1
    sys.stdout.write(count)
