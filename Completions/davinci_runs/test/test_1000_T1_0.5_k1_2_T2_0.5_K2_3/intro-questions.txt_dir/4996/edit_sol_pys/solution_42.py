import sys

message = sys.stdin.readline().strip().lower()
key = sys.stdin.readline().strip().lower()

output = ""
for i in range(len(message)):
    if (i % 2 == 0):
        output += chr((ord(message[i]) - ord(key[i]) + 26) % 26 + ord('a'))
    else:
        output += chr((ord(message[i]) - ord(key[i]) - 26) % 26 + ord('a'))
print(output)
