

N = int(input())

for i in range(N):
    P = int(input())
    if len(str(P)) == 2:  # 如果輸入的數字是兩位數
        print(int(str(P)[0])**int(str(P)[1])+int(str(P)[1])**int(str(P)[0]), end="")  # 呼叫出第一個數字的次方第二個數字，再加上第二個數字的次方第一個數字
    else:
        print(int(str(P)[0])**int(str(P)[1])+int(str(P)[1])**int(str(P)[2])+int(str(P)[2])**int(str(P)[0]), end="")  # 呼叫出第一個數字的次方第二個數字，再加上第二個數字的次方第三個數字，最後加上第三個數字的次方第一個數字
    if i < N-1:  # 如果還沒到最後一個數字
        print("+", end="")
