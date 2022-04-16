

input_num = int(input())


def is_same(num):
    for i in range(3):
        if num[i] == num[i+1]:
            return True
    return False


for i in range(3):
    if input_num[i] == input_num[i+1]:
        print("Yes")
        exit()
print("No")
