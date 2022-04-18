

# SOLUTION

# socks, capacity, colorDiff = [int(x) for x in input().split()]
# colors = [int(x) for x in input().split()]

# colors.sort()

# count = 0

# for i in range(socks):
#     if i == 0 or colors[i] - colors[i - 1] > colorDiff:
#         count += 1

# if count % capacity == 0:
#     print(count // capacity)
# else:
#     print(count // capacity + 1)


# n, m = map(int, input().split())

# if n == 1:
#     print(1)
# elif n == 2:
#     print(min(4, (m + 1) // 2))
# else:
#     if m >= 7:
#         print(m - 2)
#     else:
#         print(min(4, m))


# n, m = map(int, input().split())

# for i in range(1, n, 2):
#     print(str('.|.' * i).center(m, '-'))
# print('WELCOME'.center(m, '-'))
# for i in range(n - 2, -1, -2):
#     print(str('.|.' * i).center(m, '-'))


# for i in range(1, n, 2):
#     print((c * i).center(m, '-'))
# print(w.center(m, '-'))
# for i in range(n - 2, -1, -2):
#     print((c * i).center(m, '-'))


# n, m = map(int, input().split())


# def print_rangoli(size):
#     width = 4 * size - 3
#     string = 'abcdefghijklmnopqrstuvwxyz'
#     for i in range(1, size + 1):
#         s = "-".join(string[size - 1:size - i:-1] + string[size - i:size])
#         print(s.center(width, "-"))
#     for i in range(size - 1, 0, -1):
#         s = "-".join(string[size - 1:size - i:-1] + string[size - i:size])
#         print(s.center(width, "-"))


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# import string
# alpha = string.ascii_lowercase


# def print_rangoli(size):
#     L = []
#     for i in range(size):
#         s = "-".join(alpha[i:size])
#         L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
#     print('\n'.join(L[:0:-1]+L))


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# import string


# def print_rangoli(size):
#     n = size
#     alpha = string.ascii_lowercase
#     L = []
#     for i in range(n):
#         s = "-".join(alpha[i:n])
#         L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
#     print('\n'.join(L[:0:-1]+L))


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# import string


# def print_rangoli(size):
#     n = size
#     alpha = string.ascii_lowercase
#     L = []
#     for i in range(n):
#         s = "-".join(alpha[i:n])
#         L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
#     print('\n'.join(L[:0:-1]+L))


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)
