'''

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())
puzzle = [list(input()) for _ in range(m)]

for i in range(u):
    print('#' + '.' * (n + l + r) + '#')
for i in range(m):
    print('#' + '.' * l + ''.join(puzzle[i]) + '.' * r + '#')
for i in range(d):
'''

'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1:
            print('*', end='')
        elif j == 0 or j == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

'''

'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''

'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or j == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''

'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''

'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1 or i == n // 2 or j == n // 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''

'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1 or i == n // 2 or j == n // 2 or i == j + 1 or i + j == n - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''

'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1 or i == n // 2 or j == n // 2 or i == j + 1 or i + j == n - 2 or i == j - 1 or j == i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''

'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1 or i == n // 2 or j == n // 2 or i == j + 1 or i + j == n - 2 or i == j - 1 or j == i - 1 or i == j + 2 or i + j == n - 3:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''

'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1 or i == n // 2 or j == n // 2 or i == j + 1 or i + j == n - 2 or i == j - 1 or j == i - 1 or i == j + 2 or i + j == n - 3 or i == j - 2 or j == i - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''

'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1 or i == n // 2 or j == n // 2 or i == j + 1 or i + j == n - 2 or i == j - 1 or j == i - 1 or i == j + 2 or i + j == n - 3 or i == j - 2 or j == i - 2 or i == j - 3 or j == i - 3:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''

'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1 or i == n // 2 or j == n // 2 or i == j + 1 or i + j == n - 2 or i == j - 1 or j == i - 1 or i == j + 2 or i + j == n - 3 or i == j - 2 or j == i - 2 or i == j - 3 or j == i - 3 or i == j + 3 or i + j == n - 4:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''

'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1 or i == n // 2 or j == n // 2 or i == j + 1 or i + j == n - 2 or i == j - 1 or j == i - 1 or i == j + 2 or i + j == n - 3 or i == j - 2 or j == i - 2 or i == j - 3 or j == i - 3 or i == j + 3 or i + j == n - 4 or i == j - 4 or j == i - 4:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''

'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1 or i == n // 2 or j == n // 2 or i == j + 1 or i + j == n - 2 or i == j - 1 or j == i - 1 or i == j + 2 or i + j == n - 3 or i == j - 2 or j == i - 2 or i == j - 3 or j == i - 3 or i == j + 3 or i + j == n - 4 or i == j - 4 or j == i - 4 or i == j + 4 or i + j == n - 5 or i == j - 5 or j == i - 5:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''
    print('#' + '.' * (n + l + r) + '#')
