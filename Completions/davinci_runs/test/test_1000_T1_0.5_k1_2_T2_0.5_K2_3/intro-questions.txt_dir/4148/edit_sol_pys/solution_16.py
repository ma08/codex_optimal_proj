import sys

#include <stdio.h>


n = int(sys.stdin.readline()) #input the number of shift
s = sys.stdin.readline() #input the string

for i in range(len(s)): #loop for each letter in the string
    if ord(s[i]) + n > ord('Z'): #if the letter is shifted over the alphabet
        print(chr(ord(s[i]) + n - 26), end="") #print the letter with the shift minus 26
    else:
        print(chr(ord(s[i]) + n), end="")
