

length = input()
file_name = input()

count = 0
for i in range(2, length):
    if file_name[i-2] == file_name[i-1] and file_name[i-1] == file_name[i]:
        count += 1

print(count)
