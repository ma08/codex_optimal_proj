

import sys

message = sys.stdin.readline().strip()
key = sys.stdin.readline().strip()

output = ""
for i in range(len(message)):
    if (i % 2 == 0):
        output += chr((ord(message[i]) - ord(key[i]) + 26) % 26 + ord('A')) # + 26 to avoid negative numbers
    else:
        output += chr((ord(message[i]) - ord(key[i]) - 26) % 26 + ord('A')) # - 26 to avoid negative numbers
print(output)
