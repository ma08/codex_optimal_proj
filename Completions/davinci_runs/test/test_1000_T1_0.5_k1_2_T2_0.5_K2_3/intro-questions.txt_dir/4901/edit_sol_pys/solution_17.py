#!/usr/bin/env python3

message = input()
half1 = message[:len(message)//2] # first half of message
half2 = message[len(message)//2:] # second half of message

sum1 = 0 # sum of values of first half
sum2 = 0 # sum of values of second half
for i in range(len(half1)):
    sum1 += ord(half1[i]) - ord('A')
    sum2 += ord(half2[i]) - ord('A')
sum1 = sum1 % 26 # mod 26
sum2 = sum2 % 26 # mod 26

new1 = "" # new first half
new2 = "" # new second half
for i in range(len(half1)):
    new1 += chr(((ord(half1[i]) - ord('A') + sum1) % 26) + ord('A'))
    new2 += chr(((ord(half2[i]) - ord('A') + sum2) % 26) + ord('A'))

final = "" # final message
for i in range(len(new1)):
    final += chr(((ord(new1[i]) - ord('A') + ord(new2[i]) - ord('A')) % 26) + ord('A'))

print(final)
