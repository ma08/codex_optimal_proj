

N = int(input())

if N % 9 == 0:
  print('Yes')
else:
  print('No')


"""

def is_multiple_of_9(n):
    if n < 9:
        return n == 9
    return is_multiple_of_9(sum(map(int, str(n))))

print('Yes' if is_multiple_of_9(int(input())) else 'No')

"""
