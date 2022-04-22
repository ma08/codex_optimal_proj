

n = int(input())
file_name = input()

print(sum([file_name[i-2] == file_name[i-1] == file_name[i] for i in range(2, n)]))
