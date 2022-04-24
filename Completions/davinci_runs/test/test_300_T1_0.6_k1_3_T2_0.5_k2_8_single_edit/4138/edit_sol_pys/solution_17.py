
q = int(input())

def get_digit(k):
    if k == 1:
        return 1
    if k == 2:
        return 1
    if k == 3:
        return 2
    if k == 4:
        return 1
    if k == 5:
        return 2
    if k == 6:
        return 3
    if k == 7:
        return 1
    if k == 8:
        return 2
    if k == 9:
        return 3
    if k == 10:
        return 4
    if k == 11:
        return 1
    if k == 12:
        return 2
    if k == 13:
        return 3
    if k == 14:
        return 4
    if k == 15:
        return 5
    if k == 16:
        return 1
    if k == 17:
        return 2
    if k == 18:
        return 3
    if k == 19:
        return 4
    if k == 20:
        return 5
    if k == 21:
        return 6
    if k == 22:
        return 1
    if k == 23:
        return 2
    if k == 24:
        return 3
    if k == 25:
        return 4
    if k == 26:
        return 5
    if k == 27:
        return 6
    if k == 28:
        return 7
    if k == 29:
        return 1
    if k == 30:
        return 2
    if k == 31:
        return 3
    if k == 32:
        return 4
    if k == 33:
        return 5
    if k == 34:
        return 6
    if k == 35:
        return 7
    if k == 36:
        return 8
    if k == 37:
        return 1
    if k == 38:
        return 2
    if k == 39:
        return 3
    if k == 40:
        return 4
    if k == 41:
        return 5
    if k == 42:
        return 6
    if k == 43:
        return 7
    if k == 44:
        return 8
    if k == 45:
        return 9
    if k == 46:
        return 1
    if k == 47:
        return 2
    if k == 48:
        return 3
    if k == 49:
        return 4
    if k == 50:
        return 5
    if k == 51:
        return 6
    if k == 52:
        return 7
    if k == 53:
        return 8
    if k == 54:
        return 9
    if k == 55:
        return 10
    if k == 56:
        return 0
    if k == 57:
        return 1
    if k == 58:
        return 2
    if k == 59:
        return 3

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
