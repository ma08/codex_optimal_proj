

N = input()

if int(N) % 9 == 0:
  print('Yes')
else:
  print('No')
# python3

"""

def is_multiple_of_9(n):
    if n < 9:
        return n == 0
    return is_multiple_of_9(sum(map(int, str(n))))

print('Yes' if is_multiple_of_9(int(input())) else 'No')

"""
