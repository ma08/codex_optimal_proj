

N = int(input())  # input

if N % 4 == 0 or N % 7 == 0:  # if N is divisible by 4 or 7
    print("Yes")  # print Yes
elif N % 11 == 0:  # if N is divisible by 11
    print("Yes")  # print Yes
else:  # if none of the above are true
    print("No")  # print No
