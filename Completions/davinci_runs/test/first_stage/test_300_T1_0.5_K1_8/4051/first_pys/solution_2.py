

input_list = input().split(' ')
input_list = [int(i) for i in input_list]

for i in range(len(input_list)):
    if i == len(input_list) - 1:
        break
    if input_list[i] + 2 <= input_list[i+1]:
        print("NO")
        break
else:
    print("YES")