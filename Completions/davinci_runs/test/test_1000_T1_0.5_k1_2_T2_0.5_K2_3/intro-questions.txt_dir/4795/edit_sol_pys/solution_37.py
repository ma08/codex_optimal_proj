

N = int(input())  # N is the number of test cases

for i in range(N):
    P = int(input())  # P is the input number
    if len(str(P)) == 2:  # if the input number is two digits
        print(int(str(P)[0])**int(str(P)[1])+int(str(P)[1])**int(str(P)[0]), end="")  # print the sum of the first digit to the power of the second digit and the second digit to the power of the first digit, without a new line
    else:
        print(int(str(P)[0])**int(str(P)[1])+int(str(P)[1])**int(str(P)[2])+int(str(P)[2])**int(str(P)[0]), end="")  # print the sum of the first digit to the power of the second digit, the second digit to the power of the third digit and the third digit to the power of the first digit, without a new line
    if i < N-1:  # if it is not the last iteration
        print("+", end="")  # print a plus sign
