

k = int(input())

# initialize i to the number of digits in the number k
i = len(str(k))

while True:
    # calculate the number with i digits
    num = int('7' * i)
    # if it's a multiple of k, print the number of digits and break
    if num % k == 0:
        print(i)
        break
    # otherwise, increase the number of digits by 1
    i += 1