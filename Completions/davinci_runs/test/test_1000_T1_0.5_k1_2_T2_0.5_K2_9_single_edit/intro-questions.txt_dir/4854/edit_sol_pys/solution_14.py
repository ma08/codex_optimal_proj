

#message = "1 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8"

message = input()
message = message.split(" ")

for i in range(0,len(message)):
    message[i] = int(message[i])

message.sort()

#print(message)

count = 1

for i in range(0,len(message)):
    if i != len(message) - 1:
        if message[i] == message[i+1]:
            count += 1
        else:
            print(message[i], end = " ")
            count = 1
    else:
        print(message[i], end = "")
