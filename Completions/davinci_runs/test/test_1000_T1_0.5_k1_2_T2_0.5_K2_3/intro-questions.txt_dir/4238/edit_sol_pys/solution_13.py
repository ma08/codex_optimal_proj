
# ここでは、入力された数字の各桁の和を求め、その9の倍数であるか判定している
N = input()  # input a number

if sum(map(int, N)) % 9 == 0:
    print("Yes")
else:
    print("No")
