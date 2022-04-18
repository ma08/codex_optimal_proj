
# while loop to find minimum number
n = int(input()) # input number

while True:
    n += 1 # increment n
    if n % sum([int(i) for i in str(n)]) == 0: # check if n is divisible by the sum of its digits
        print(n)
        break
