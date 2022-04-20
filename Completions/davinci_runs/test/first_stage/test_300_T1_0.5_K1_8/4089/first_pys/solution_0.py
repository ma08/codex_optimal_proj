

import sys
import math

# N is an integer. 1 <= N <= 1000000000000001
N = int(sys.stdin.readline())

# the number of digits of the answer
# (the number of times the alphabet has to be repeated)
digits = int(math.log(N, 26))
# the number of digits of the answer
# (the number of times the alphabet has to be repeated)
if N > 26 ** digits:
    digits += 1

# the number of dogs with a name of length 'digits'
num_dogs_with_digits = 26 ** digits

# the number of dogs with a name of length 'digits - 1'
num_dogs_with_digits_minus_1 = 26 ** (digits - 1)

# the number of dogs with a name of length 'digits - 1'
# that precede the dog we are looking for
num_dogs_with_digits_minus_1_before_N = (N - 1) // num_dogs_with_digits_minus_1

# the number of dogs with a name of length 'digits'
# that precede the dog we are looking for
num_dogs_with_digits_before_N = num_dogs_with_digits_minus_1_before_N * num_dogs_with_digits_minus_1

# the index of the letter in the alphabet
alphabet_index = (N - num_dogs_with_digits_before_N - 1) // num_dogs_with_digits_minus_1

# the letter in the alphabet corresponding to the index
alphabet_letter = chr(ord('a') + alphabet_index)

# the answer
ans = ""
for i in range(digits - 1):
    ans += alphabet_letter

sys.stdout.write(ans)