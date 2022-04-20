

import sys

n = int(sys.stdin.readline())

# if n % 25 == 0:
#     print(0)
#     exit()

# if n % 5 == 0:
#     print(1)
#     exit()

# if n % 25 == 5 or n % 25 == 0:
#     print(2)
#     exit()

# if n % 5 == 1:
#     print(3)
#     exit()

# if n % 5 == 2 or n % 5 == 3 or n % 5 == 4:
#     print(4)
#     exit()

# print(-1)

if n % 25 == 0:
    print(0)
    exit()

if n % 5 == 0:
    print(1)
    exit()

if n % 25 == 5 or n % 25 == 0:
    print(2)
    exit()

if n % 5 == 1:
    print(3)
    exit()

if n % 5 == 2 or n % 5 == 3 or n % 5 == 4:
    print(4)
    exit()

print(-1)