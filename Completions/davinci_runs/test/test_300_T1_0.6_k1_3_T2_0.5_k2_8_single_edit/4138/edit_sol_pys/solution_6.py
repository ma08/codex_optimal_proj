

q = int(input())

def get_digit(k):

    k -= 1

    #number of all digits before k
    digit_sum = 0
    for i in range(1, 100):
        digit_sum += 9 * i * 10 ** (i - 1)
        if k < digit_sum:
            break

    k -= digit_sum

    #number of digits in the number which contains k
    number = k // i
    k -= number * i

    #number that contains k
    number += 10 ** (i - 1)
    #print("number: ", number)

    #print("k: ", k)
    k -= 1
    #print("k: ", k)

    digit = number // (10 ** k)
    digit %= 10

    return digit


for i in range(q):
    k = int(input())
    print(get_digit(k))
