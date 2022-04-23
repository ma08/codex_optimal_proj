

import sys

sys.setrecursionlimit(10 ** 6)

q = int(input())

def get_digit(k):
    if k < 60:
        return [1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3][k]

    #print("k: ", k)
    k -= 1
    #print("k: ", k)

    #number of all digits before k
    digit_sum = 0
    for i in range(1, 100):
        digit_sum += 9 * i * 10 ** (i - 1)
        #print("digit_sum: ", digit_sum, "i: ", i)
        if k < digit_sum:
            #print("digit_sum: ", digit_sum, "i: ", i)
            break


    #print("digit_sum: ", digit_sum, "i: ", i)
    #print("k: ", k)
    k -= digit_sum
    #print("k: ", k)

    #number of digits in the number which contains k
    number = k // i
    #print("number: ", number)

    #print("k: ", k)
    k -= number * i
    #print("k: ", k)

    #number that contains k
    number += 10 ** (i - 1)
    #print("number: ", number)

    #print("k: ", k)
    k -= 1
    #print("k: ", k)

    digit = number // (10 ** k)
    digit %= 10
    #print("digit: ", digit)

    return digit


for i in range(q):
    k = int(input())
    print(get_digit(k))
