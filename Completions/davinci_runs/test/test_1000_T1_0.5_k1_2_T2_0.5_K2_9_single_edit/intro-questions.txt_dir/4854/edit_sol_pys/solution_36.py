

message = input()
message = message.split(" ")

for i in range(0,len(message)):
    message[i] = int(message[i])

#message.sort()

#print(message)

for i in range(0,len(message)):
    for j in range(i+1,len(message)):
        if message[i] == message[j]:
            message[j] = -1

for i in range(0,len(message)):
    if message[i] != -1:
        print(message[i], end = " ")
