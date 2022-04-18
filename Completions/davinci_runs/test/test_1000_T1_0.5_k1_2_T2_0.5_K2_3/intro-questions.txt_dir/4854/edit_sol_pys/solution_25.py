
#input
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
            print(message[i], end = "")
            count = 1
    else:
        print(message[i], end = "")
