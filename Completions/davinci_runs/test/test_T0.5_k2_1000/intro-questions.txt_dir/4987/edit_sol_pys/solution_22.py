from sys import stdin

N, M = map(int, stdin.readline().split())

file_list = []
for _ in range(N):
    file_list.append(stdin.readline().strip())

for _ in range(M):
    command = stdin.readline().strip()

    if command == 'ls':
        print(' '.join(file_list))

    elif command == 'touch':
        file_name = stdin.readline().strip()

        if file_name in file_list:
            print(f'{file_name} is already exist')
        else:
            file_list.append(file_name)

    elif command == 'rm':
        file_name = stdin.readline().strip()

        if file_name in file_list:
            file_list.remove(file_name)
        else:
            print(f'{file_name} is not exist')

    elif command == 'rename':
        old_name, new_name = stdin.readline().strip().split()

        if old_name in file_list:
            file_list[file_list.index(old_name)] = new_name
        else:
            print(f'{old_name} is not exist')
