

q = int(input())

def get_digit(k):

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
