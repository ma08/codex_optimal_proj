
n = int(input())  # number of files
file_names = []
for i in range(n):
    file_names.append(input())
    
for file_name in file_names:
    count = 0
    for i in range(2, len(file_name)):
        if file_name[i-2] == file_name[i-1] == file_name[i]:
            count += 1
    print(count)
