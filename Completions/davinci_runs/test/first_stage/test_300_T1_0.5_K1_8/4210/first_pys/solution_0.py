

from sys import stdin

n, k = [int(x) for x in stdin.readline().split()]
a = [int(x) for x in stdin.readline().split()]

# a = [45, 1, 10, 12, 11, 7]
# n, k = 6, 11

# a = [2, 78, 4, 10]
# n, k = 4, 2

# a = [3, 7, 19, 3, 3]
# n, k = 5, 2


def get_digits(a):
    return len(str(a))


def concatenate(a, b):
    return int(str(a) + str(b))


def is_divisible(a, b, k):
    return concatenate(a, b) % k == 0


def get_divisors(k):
    divisors = []

    for i in range(1, k + 1):
        if k % i == 0:
            divisors.append(i)

    return divisors


def get_counts(a):
    counts = {}

    for num in a:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1

    return counts


def get_count_of_pairs_with_divisors(a, k):
    """
    Return count of pairs of numbers that when concatenated are divisible by k
    """
    a_counts = get_counts(a)
    k_divisors = get_divisors(k)

    count = 0

    for divisor in k_divisors:
        divisor_count = 0
        for num, num_count in a_counts.items():
            if num % divisor == 0:
                divisor_count += num_count

        count += (divisor_count * (divisor_count - 1)) / 2

    return count


def get_count_of_pairs_without_divisors(a, k):
    """
    Return count of pairs of numbers that when concatenated are not divisible by k
    """
    count = 0

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if not is_divisible(a[i], a[j], k):
                count += 1

    return count


def get_count_of_pairs(a, k):
    """
    Return count of pairs of numbers that when concatenated are divisible by k
    """
    return get_count_of_pairs_with_divisors(a, k) + get_count_of_pairs_without_divisors(a, k)


print(int(get_count_of_pairs(a, k)))