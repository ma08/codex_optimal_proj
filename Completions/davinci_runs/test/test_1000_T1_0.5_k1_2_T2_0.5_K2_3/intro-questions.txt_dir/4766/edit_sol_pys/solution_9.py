N = int(input())
for i in range(N):
    command = input()
    if command[:10] == "Simon says":
        print(command[10:])
