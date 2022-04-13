

# letters = [0 for _ in range(26)]

# for letter in input():
#     letters[ord(letter) - ord('a')] += 1

# print(sum(letter % 2 for letter in letters))

# def print_formatted(number):
#     # your code goes here
#     for i in range(1, number + 1):
#         print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=len("{0:b}".format(number))))


# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


# def print_rangoli(size):
#     # your code goes here
#     for i in range(size):
#         s = "-".join(chr(ord('a') + size - j - 1) for j in range(i + 1))
#         print((s + s[::-1][1:]).center(n * 4 - 3, '-'))

#     for i in range(n - 1):
#         s = "-".join(chr(ord('a') + size - j - 1) for j in range(size - i - 1))
#         print((s + s[::-1][1:]).center(n * 4 - 3, '-'))


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# def print_rangoli(size):
#     # your code goes here
#     for i in range(size):
#         s = "-".join(chr(ord('a') + size - j - 1) for j in range(i + 1))
#         print((s + s[::-1][1:]).center(n * 4 - 3, '-'))

#     for i in range(n - 1):
#         s = "-".join(chr(ord('a') + size - j - 1) for j in range(size - i - 1))
#         print((s + s[::-1][1:]).center(n * 4 - 3, '-'))


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# import string

# alpha = string.ascii_lowercase


# def print_rangoli(size):
#     L = []
#     for i in range(size):
#         s = "-".join(alpha[i:size])
#         L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
#     print('\n'.join(L[:0:-1] + L))


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# import string

# alpha = string.ascii_lowercase


# def print_rangoli(size):
#     L = []
#     for i in range(size):
#         s = "-".join(alpha[i:size])
#         L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
#     print('\n'.join(L[:0:-1] + L))


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# import math
# import os
# import random
# import re
# import sys

# Complete the migratoryBirds function below.
# def migratoryBirds(arr):
#     # Complete this function
#     count = [0] * 6
#     for i in arr:
#         count[i] += 1
#     return count.index(max(count))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = migratoryBirds(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()


# import math
# import os
# import random
# import re
# import sys

# Complete the migratoryBirds function below.
# def migratoryBirds(arr):
#     # Complete this function
#     count = [0] * 6
#     for i in arr:
#         count[i] += 1
#     return count.index(max(count))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = migratoryBirds(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()


# import math
# import os
# import random
# import re
# import sys

# Complete the migratoryBirds function below.
# def migratoryBirds(arr):
#     # Complete this function
#     count = [0] * 6
#     for i in arr:
#         count[i] += 1
#     return count.index(max(count))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = migratoryBirds(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()


# import math
# import os
# import random
# import re
# import sys

# Complete the migratoryBirds function below.
# def migratoryBirds(arr):
#     # Complete this function
#     count = [0] * 6
#     for i in arr:
#         count[i] += 1
#     return count.index(max(count))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = migratoryBirds(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()


# import math
# import os
# import random
# import re
# import sys

# Complete the migratoryBirds function below.
# def migratoryBirds(arr):
#     # Complete this function
#     count = [0] * 6
#     for i in arr:
#         count[i] += 1
#     return count.index(max(count))


# if __name
