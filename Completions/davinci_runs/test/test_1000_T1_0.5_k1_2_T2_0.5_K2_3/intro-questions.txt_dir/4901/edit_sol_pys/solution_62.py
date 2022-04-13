#!/usr/bin/env python3

def main():
    message = input()
    half1 = message[:len(message)//2] # first half
    half2 = message[len(message)//2:] # second half
    
    sum1 = 0 # sum of first half
    sum2 = 0 # sum of second half
    for i in range(len(half1)):
        sum1 += ord(half1[i]) - ord('A')
        sum2 += ord(half2[i]) - ord('A')
    sum1 = sum1 % 26 # mod 26
    sum2 = sum2 % 26 # mod 26
    
    new1 = "" # first half
    new2 = "" # second half
    for i in range(len(half1)):
        new1 += chr(((ord(half1[i]) - ord('A') + sum1) % 26) + ord('A'))
        new2 += chr(((ord(half2[i]) - ord('A') + sum2) % 26) + ord('A'))
    
    final = "" # message
    for i in range(len(new1)):
        final += chr(((ord(new1[i]) - ord('A') + ord(new2[i]) - ord('A')) % 26) + ord('A'))
    
    print(final)

if __name__ == "__main__":
    main()
