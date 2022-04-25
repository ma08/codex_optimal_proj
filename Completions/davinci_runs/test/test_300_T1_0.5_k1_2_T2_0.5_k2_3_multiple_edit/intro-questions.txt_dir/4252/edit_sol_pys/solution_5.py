

n = int(input())
file_name = input()
# for i in file_name:
#     if i == 'xxx':
#         count += 1
count = 0
for i in range(2, n):
    if file_name[i-2] == file_name[i-1] == file_name[i]:
        count += 1


print(count)
