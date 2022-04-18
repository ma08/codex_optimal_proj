input_num = input()

for i in range(3):
    if input_num[i] == input_num[i+1]:
        print("Yes")
        exit()
print("No")
