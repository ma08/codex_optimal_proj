

# ---- Solution 1 ----
# Dog number: 1, 2, ..., 26, 27, 28, ..., 702, 703, 704, ..., 18278, 18279, 18280, ..., 475254, 475255, 475256, ...
# Dog name:   a, b, ..., z, aa, ab, ..., zz, aaa, aab, ..., zzz, aaaa, aaab, ..., zzzz, aaaaa, aaaab, ...
#
# Dog name of length 1: 26
# Dog name of length 2: 26^2
# Dog name of length 3: 26^3
# ...
# Dog name of length n: 26^n
#
# Dog number of length 1: 1, 2, ..., 26
# Dog number of length 2: 27, 28, ..., 702
# Dog number of length 3: 703, 704, ..., 18278
# ...
# Dog number of length n: 26^(n-1) + 1, 26^(n-1) + 2, ..., 26^n
#
# Dog number N:
# 1. Find the n where n is the length of the dog name
# 2. Find the dog name of length n
# 3. Find the dog name of dog number N

def find_dog_name(n):
    # find n
    n_length = 1
    while True:
        if n <= 26 ** n_length:
            break
        n_length += 1

    # find dog name of length n
    dog_name = ''
    for i in range(n_length):
        # find the dog name of length n
        if n > 26 ** n_length:
            n -= 26 ** n_length
            dog_name += 'z'
        else:
            dog_name += chr(ord('a') + n // 26 ** (n_length - 1) - 1)
            n = n % 26 ** (n_length - 1)
            break

    return dog_name

# ---- Solution 2 ----
# Dog number: 1, 2, ..., 26, 27, 28, ..., 702, 703, 704, ..., 18278, 18279, 18280, ..., 475254, 475255, 475256, ...
# Dog name:   a, b, ..., z, aa, ab, ..., zz, aaa, aab, ..., zzz, aaaa, aaab, ..., zzzz, aaaaa, aaaab, ...
#
# Dog name of length 1: 26
# Dog name of length 2: 26^2
# Dog name of length 3: 26^3
# ...
# Dog name of length n: 26^(n-1)
#
# Dog number of length 1: 1, 2, ..., 26
# Dog number of length 2: 27, 28, ..., 702
# Dog number of length 3: 703, 704, ..., 18278
# ...
# Dog number of length n: 26^(n-1) + 1, 26^(n-1) + 2, ..., 26^n
#
# Dog number N:
# 1. Find the n where n is the length of the dog name
# 2. Find the dog name of length n
# 3. Find the dog name of dog number N

def find_dog_name_2(n):
    # find n
    n_length = 1
    while True:
        if n <= 26 ** n_length:
            break
        n_length += 1

    # find dog name of length n
    dog_name = ''
    for i in range(n_length):
        # find the dog name of length n
        if n > 26 ** n_length:
            n -= 26 ** n_length
            dog_name += 'z'
        else:
            dog_name += chr(ord('a') + n // 26 ** (n_length - 1) - 1)
            n = n % 26 ** (n_length - 1)
            break

    return dog_name


def main():
    n = int(input())
    print(find_dog_name_2(n))


if __name__ == '__main__':
    main()
