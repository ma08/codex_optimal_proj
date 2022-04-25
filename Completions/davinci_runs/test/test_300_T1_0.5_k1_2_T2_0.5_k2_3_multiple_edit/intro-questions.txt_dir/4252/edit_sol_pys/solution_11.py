

n = int(input())
file_name = input()

count = 0
for i in range(2, n):
    if file_name[i-2] == file_name[i-1] == file_name[i]:  # if the three consecutive characters are the same
        count += 1




print(count)
