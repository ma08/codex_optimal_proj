

#n = int(input())
#l = [int(x) for x in input().split()]

#l = [21,34,18,9]
#n = len(l)

def max_javelin(l):
    if len(l) == 1:
        return l[0]
    else:
        l = sorted(l)
        return l[-1] + max_javelin(l[:-1]) - 1




def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

#print(is_palindrome("racecar"))
#print(is_palindrome("a"))
#print(is_palindrome(""))
#print(is_palindrome("ab"))
#print(is_palindrome("aa"))
#print(is_palindrome("aba"))
#print(is_palindrome("abba"))
#print(is_palindrome("abcba"))
#print(is_palindrome("abccba"))
#print(is_palindrome("abcdba"))



def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return reverse_string(s[1:]) + s[0]

#print(reverse_string("abcdefg"))



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#print(factorial(0))
#print(factorial(1))
#print(factorial(3))
#print(factorial(5))



def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)

#print(sum_digits(0))
#print(sum_digits(1))
#print(sum_digits(3))
#print(sum_digits(5))
#print(sum_digits(10))
#print(sum_digits(123))
#print(sum_digits(12345))



def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(0))
#print(fibonacci(1))
#print(fibonacci(2))
#print(fibonacci(3))
#print(fibonacci(4))
#print(fibonacci(5))
#print(fibonacci(6))



def is_power_of(x, n):
    if x == n:
        return True
    elif x < n:
        return False
    else:
        return is_power_of(x/n, n)

#print(is_power_of(1, 2))
#print(is_power_of(2, 2))
#print(is_power_of(3, 2))
#print(is_power_of(4, 2))
#print(is_power_of(5, 2))
#print(is_power_of(8, 2))
#print(is_power_of(16, 2))
#print(is_power_of(17, 2))
#print(is_power_of(1, 3))
#print(is_power_of(3, 3))
#print(is_power_of(9, 3))
#print(is_power_of(27, 3))
#print(is_power_of(28, 3))



def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

#print(gcd(1, 1))
#print(gcd(2, 1))
#print(gcd(3, 1))
#print(gcd(4, 1))
#print(gcd(5, 1))
#print(gcd(1, 2))
#print(gcd(2, 2))
#print(gcd(3, 2))
#print(gcd(4, 2))
#print(gcd(5, 2))
#print(gcd(1, 3))
#print(gcd(3, 3))
#print(gcd(5, 3))
#print(gcd(9, 3))
#print(gcd(15, 3))
#print(gcd(16, 8))
#print(gcd(16, 4))
#print(gcd(16, 2))
#print(gcd(16, 1))
#print(gcd(16, 3))
#print(gcd(16, 5))
#print(gcd(16, 7))
#print(gcd(16, 9))
#print(gcd(16, 11))
#print(gcd(16, 13))
#print(gcd(16, 15))
#print(max_javelin(l))
