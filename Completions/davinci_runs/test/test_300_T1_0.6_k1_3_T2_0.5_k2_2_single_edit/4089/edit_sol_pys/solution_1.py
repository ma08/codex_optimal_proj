

from sys import stdin

def get_name(n):
    # As per the problem statement, the names for numbers 1 to 26 are mapped directly to the alphabets a to z.
    # Hence we can directly return the name for numbers 1 to 26.
    if n <= 26:
        return chr(96 + n)
    else:
        # We need to calculate the name for the remaining numbers.
        # For numbers from 27 to 702, we need to use the formula
        # name = 26 * (n-1) + (n-27)
        # For numbers from 703 to 18278, we need to use the formula
        # name = 26 * 26 * (n-1) + 26 * (n-703) + (n-703)
        # For numbers from 18279 to 475254, we need to use the formula
        # name = 26 * 26 * 26 * (n-1) + 26 * 26 * (n-18279) + 26 * (n-18279) + (n-18279)
        # For numbers from 475255 to 1000000000000001, we need to use the formula
        # name = 26 * 26 * 26 * 26 * (n-1) + 26 * 26 * 26 * (n-475255) + 26 * 26 * (n-475255) + 26 * (n-475255) + (n-475255)
        #
        # From the above formulae, we can see that the number of digits in the name is one more than the
        # number of letters used in the name. Hence, for example, the number of digits in the name for dog
        # number 5 is 2 and the number of letters used in the name 'aaa' is 2.
        # Hence, we can find out the number of digits in the name by dividing the number by the number of
        # letters used in the name.
        # We can find the number of letters used in the name by taking the logarithm of the number in base 26.
        # The name consists of the letters 'a' to 'z' and the letters are repeated in the order 'a', 'b', 'c' ...
        # till 'z' and then starting again from 'a'.
        # To find the letter at a particular index, we divide the index by 26 and take the remainder.
        # For example, to find the letter at the index 101, we divide 101 by 26 to get 3. The remainder is 19.
        # Hence the letter at the index 101 is the letter at the index 19, which is 's'.
        # Since the number of letters used in the name is the same as the number of digits in the name, we can
        # use the same logic to find the number of letters used in the name.
        # We divide the number by 26 and take the remainder to get the number of letters used in the name.
        name_len = n % 26 or 26
        # We divide the number by 26 to get the number of letters used in the name.
        name = ''
        # We loop from the number of digits in the name to 1 to get the name for the dog number.
        for i in range(name_len, 0, -1):
            # We divide the number by the number of letters used in the name and take the remainder to get the
            # index at which the letter is placed.
            # We then add the letter at the index to the name.
            name += chr(96 + (n % (26 ** i) / (26 ** (i - 1))))
        return name

if __name__ == '__main__':
    n = int(stdin.readline())
    print get_name(n)
