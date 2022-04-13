

N = int(input())

for i in range(N):
    P = int(input())
    if len(str(P)) == 2:
        print(int(str(P)[0])**int(str(P)[1])+int(str(P)[1])**int(str(P)[0]), end="")  # if lenght of number is 2
    else:
        print(int(str(P)[0])**int(str(P)[1])+int(str(P)[1])**int(str(P)[2])+int(str(P)[2])**int(str(P)[0]), end="")  # if length of number is 3
    if i < N-1:
        print("+", end="")
