def check_consecutive(file_name, n):
    count = 0
    for i in range(2, n):
        if file_name[i-2] == file_name[i-1] == file_name[i]:
            count += 1
    return count


n = int(input())
file_name = input()

count = 0
for i in range(2, n):
    if file_name[i-2] == file_name[i-1] == file_name[i]:
        count += 1

print(count)
