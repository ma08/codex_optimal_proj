

input_num = input() # 入力された数字をinput_numに代入する

for i in range(3):
    if input_num[i] == input_num[i+1]:
        print("Yes")
        exit()
print("No")
