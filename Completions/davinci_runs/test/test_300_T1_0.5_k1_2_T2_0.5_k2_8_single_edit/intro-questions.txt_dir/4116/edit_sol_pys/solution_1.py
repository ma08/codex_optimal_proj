

N = int(input()) # input number

if N % 2 == 0 and N % 5 == 0: # check if the number is divisible by 2 and 5
    print('Yes')
elif N % 3 == 0 and N % 3 == 0:
    print('Yes')
elif N % 2 == 0 and N % 3 == 0:
    print('Yes')
else:
    print('No')
