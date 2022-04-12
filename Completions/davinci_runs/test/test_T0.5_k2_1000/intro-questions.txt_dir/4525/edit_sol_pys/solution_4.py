def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


def get_sum_of_factors(n):
    factors = get_factors(n)
    return sum(factors)


def is_perfect_number(n):
    return n == get_sum_of_factors(n)


def get_perfect_numbers(n):
    perfect_numbers = []
    for i in range(1, n + 1):
        if is_perfect_number(i):
            perfect_numbers.append(i)
    return perfect_numbers


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_prime_numbers(n):
    primes = []
    for i in range(1, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def get_prime_factors(n):
    factors = get_factors(n)
    primes = get_prime_numbers(n)
    prime_factors = []
    for i in factors:
        if i in primes:
            prime_factors.append(i)
    return prime_factors


def get_prime_factorization(n):
    prime_factors = get_prime_factors(n)
    prime_factorization = []
    for i in prime_factors:
        if n % i == 0:
            prime_factorization.append(i)
    return prime_factorization


def get_prime_factorization_with_powers(n):
    prime_factorization = get_prime_factorization(n)
    prime_factorization_with_powers = {}
    for i in prime_factorization:
        if i in prime_factorization_with_powers:
            prime_factorization_with_powers[i] += 1
        else:
            prime_factorization_with_powers[i] = 1
    return prime_factorization_with_powers


def get_prime_factorization_with_powers_in_list(n):
    prime_factorization_with_powers = get_prime_factorization_with_powers(n)
    prime_factorization_with_powers_in_list = []
    for i in prime_factorization_with_powers:
        prime_factorization_with_powers_in_list.append(
            [i, prime_factorization_with_powers[i]])
    return prime_factorization_with_powers_in_list


def get_prime_factorization_with_powers_in_list_with_multiplicity(n):
    prime_factorization_with_powers_in_list = get_prime_factorization_with_powers_in_list(
        n)
    prime_factorization_with_powers_in_list_with_multiplicity = []
    for i in prime_factorization_with_powers_in_list:
        for j in range(i[1]):
            prime_factorization_with_powers_in_list_with_multiplicity.append(
                i[0])
    return prime_factorization_with_powers_in_list_with_multiplicity


def get_prime_factorization_with_powers_in_list_with_multiplicity_in_string(n):
    prime_factorization_with_powers_in_list_with_multiplicity = get_prime_factorization_with_powers_in_list_with_multiplicity(
        n)
    prime_factorization_with_powers_in_list_with_multiplicity_in_string = ""
    for i in prime_factorization_with_powers_in_list_with_multiplicity:
        prime_factorization_with_powers_in_list_with_multiplicity_in_string += str(
            i)
    return prime_factorization_with_powers_in_list_with_multiplicity_in_string


def get_prime_factorization_in_string(n):
    prime_factorization = get_prime_factorization(n)
    prime_factorization_in_string = ""
    for i in prime_factorization:
        prime_factorization_in_string += str(i)
    return prime_factorization_in_string


def get_prime_factorization_with_powers_in_string(n):
    prime_factorization_with_powers = get_prime_factorization_with_powers(n)
    prime_factorization_with_powers_in_string = ""
    for i in prime_factorization_with_powers:
        prime_factorization_with_powers_in_string += str(i) + "^" + str(
            prime_factorization_with_powers[i]) + " "
    return prime_factorization_with_powers_in_string


def get_prime_factorization_with_powers_in_list_in_string(n):
    prime_factorization_with_powers_in_list = get_prime_factorization_with_powers_in_list(
        n)
    prime_factorization_with_powers_in_list_in_string = ""
    for i in prime_factorization_with_powers_in_list:
        prime_factorization_with_powers_in_list_in_string += str(
            i[0]) + "^" + str(i[1]) + " "
    return prime_factorization_with_powers_in_list_in_string


def get_prime_factorization_with_powers_in_list_with_multiplicity_in_string(n):
    prime_factorization_with_powers_in_list_with_multiplicity = get_prime_factorization_with_powers_in_list_with_multiplicity(
        n)
    prime_factorization_with_powers_in_list_with_multiplicity_in_string = ""
    for i in prime_factorization_with_powers_in_list_with_multiplicity:
        prime_factorization_with_powers_in_list_with_multiplicity_in_string += str(
            i) + " "
    return prime_factorization_with_powers_in_list_with_multiplicity_in_string
