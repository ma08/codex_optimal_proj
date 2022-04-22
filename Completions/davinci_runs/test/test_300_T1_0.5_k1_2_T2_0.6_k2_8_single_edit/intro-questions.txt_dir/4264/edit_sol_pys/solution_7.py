

N = int(input())

count = 0
for i in range(1, N+1):
    count += len(str(i)) % 2



# def is_prime_number(n):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True
#     else:
#         return False


# n = int(input())
# if is_prime_number(n):
#     print("YES")
# else:
#     print("NO")

# n = int(input())
# for i in range(n):
#     print("*"*(i+1))


# n = int(input())
# for i in range(n):
#     print(" "*(n-i-1) + "*"*(i+1))


# n = int(input())
# for i in range(n):
#     print(" "*(n-i-1) + "*"*(i*2+1))


# n = int(input())
# for i in range(n):
#     print("*"*(n-i) + " "*(i*2) + "*"*(n-i))


# n = int(input())
# for i in range(n):
#     print(" "*(n-i-1) + "*"*(i*2+1))
# for i in range(n-2, -1, -1):
#     print(" "*(n-i-1) + "*"*(i*2+1))


# n = int(input())
# for i in range(n):
#     print("*"*(n-i) + " "*(i*2) + "*"*(n-i))
# for i in range(n-2, -1, -1):
#     print("*"*(n-i) + " "*(i*2) + "*"*(n-i))


# n = int(input())
# for i in range(n):
#     print(" "*(n-i-1) + "*"*(i*2+1))
# for i in range(n-2, -1, -1):
#     print(" "*(n-i-1) + "*"*(i*2+1))
# for i in range(n-2, -1, -1):
#     print(" "*(n-i-1) + "*"*(i*2+1))
# for i in range(n-2, -1, -1):
#     print(" "*(n-i-1) + "*"*(i*2+1))


# n = int(input())
# for i in range(n):
#     print(" "*(n-i-1) + "*"*(i*2+1))
# for i in range(n-2, -1, -1):
#     print(" "*(n-i-1) + "*"*(i*2+1))
# for i in range(n-2, -1, -1):
#     print(" "*(n-i-1) + "*"*(i*2+1))
# for i in range(n-2, -1, -1):
#     print(" "*(n-i-1) + "*"*(i*2+1))
# for i in range(n-2, -1, -1):
#     print(" "*(n-i-1) + "*"*(i*2+1))
# for i in range(n-2, -1, -1):
#     print(" "*(n-i-1) + "*"*(i*2+1))
print(count)
