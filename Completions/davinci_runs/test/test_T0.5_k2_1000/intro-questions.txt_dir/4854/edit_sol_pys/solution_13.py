

messages = input()
messages = messages.split(" ")

for i in range(0,len(messages)):
    messages[i] = int(messages[i])

messages.sort()

#print(messages)

count = 1

    if messages[i] == messages[i+1]:
        count += 1
    else:
        print(messages[i], end = " ") 
        count = 1
