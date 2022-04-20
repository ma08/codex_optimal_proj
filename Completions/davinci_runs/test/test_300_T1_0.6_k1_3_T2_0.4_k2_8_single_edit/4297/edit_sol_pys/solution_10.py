

#input number of test cases
T = int(input())

#loop through each test case
for i in range(T):
    #input number
    N = int(input())

    #the minimum positive integer divisible by both 2 and N
    answer = N

    #if N is even, then N is divisible by both 2 and N
    while answer % 2 != 0:
        answer += N

    print(answer)
