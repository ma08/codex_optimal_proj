

# SOLUTION
# n, k = map(int, input().split())

# if k == 1:
#     if n == 1:
#         print('YES')
#         print(n)
#     else:
#         print('NO')
# elif k == 2:
#     if n%2 == 0:
#         print('YES')
#         print(n//2, n-n//2)
#     else:
#         print('NO')
# elif k == 3:
#     if n%3 == 0:
#         print('YES')
#         print(n//3, n//3, n-2*n//3)
#     else:
#         print('NO')
# elif k > 3:
#     if n >= k and n <= 2*k-1:
#         print('YES')
#         if n >= k+2:
#             print(1, 1, n-2)
#         else:
#             print(1, n-1)
#     else:
#         print('NO')

n = int(input())

if n%2 == 1:
    print('Weird')
else:
    if n > 20:
        print('Not Weird')
    elif n >= 6:
        print('Weird')
    else:
        print('Not Weird')
