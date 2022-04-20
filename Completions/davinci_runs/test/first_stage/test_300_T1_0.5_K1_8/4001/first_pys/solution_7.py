

n = int(input())
divisors = [int(x) for x in input().split()]

# Find the number of occurrences of each divisor
occurrences = {}
for d in divisors:
    if d in occurrences:
        occurrences[d] += 1
    else:
        occurrences[d] = 1

# The number of occurrences of a number in the list of divisors is the number of
# times that number appears in the prime factorization of the original number.
# The prime factorization of the original number is the union of the prime
# factorizations of the two numbers.
#
# If a number appears an odd number of times in the list of divisors, then it
# must appear an odd number of times in the prime factorization of the original
# number. Since the prime factorization of a number is unique, this means that
# the number must appear an odd number of times in the prime factorization of
# both of the original numbers.

divisors = {d: occurrences[d] for d in occurrences if occurrences[d] % 2 == 1}

# Each number in the prime factorization of the original number must appear an
# even number of times in the list of divisors. Since each number in the prime
# factorization of the original number must appear an even number of times in
# the prime factorization of both of the original numbers, this means that each
# number in the prime factorization of both of the original numbers must appear
# an even number of times in the list of divisors.

divisors2 = {d: occurrences[d] for d in occurrences if occurrences[d] % 2 == 0}

# The prime factorization of the original number is the union of the prime
# factorizations of the two numbers.
#
# If a number appears an odd number of times in the list of divisors, then it
# must appear an odd number of times in the prime factorization of the original
# number.
#
# If a number appears an even number of times in the list of divisors, then it
# must appear an even number of times in the prime factorization of the original
# number.
#
# This means that the prime factorization of the original number is the union of
# the prime factorizations of the two numbers.
#
# The prime factorization of a number is unique, so the prime factorization of
# the original number is unique. This means that the prime factorization of the
# two numbers is also unique.
#
# This means that the two numbers can be uniquely determined from the list of
# divisors.

x = 1
y = 1
for d in divisors:
    x *= d
    y *= d
for d in divisors2:
    x *= d

print(x, y)