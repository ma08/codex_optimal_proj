
n = int(input())
file_name = input().lower()


count = 0

for i in range(2, n-1):
    if file_name[i-2] == 'x' and file_name[i-1] == 'x' and file_name[i] == 'x':
        if file_name[i+1] == 'x' or file_name[i-3] == 'x':
            continue
        else:
            count += 1

print(count)
