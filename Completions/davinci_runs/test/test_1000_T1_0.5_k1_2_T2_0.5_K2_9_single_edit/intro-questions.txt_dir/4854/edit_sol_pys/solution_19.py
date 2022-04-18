

message = input()
message = message.split(" ")

for i in range(0,len(message)):
    message[i] = int(message[i])

message.sort()

count = 1

for i in range(0, len(message)):
    if i != len(message) - 1 and count < 3:
        if message[i] == message[i+1]:
            count += 1
        elif count == 1:
            print(message[i], end = " ")
            count = 1
        elif count == 2:
            print(message[i], end = " ")
            print(message[i], end = " ")
            count = 1
    else:
        if count == 1:
            print(message[i], end = " ")
        elif count == 2:
            print(message[i], end = " ")
            print(message[i], end = " ")
