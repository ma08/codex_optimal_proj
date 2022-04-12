#!/usr/bin/python3

N = int(input())

words = []

for i in range(N):
    words.append(input())

for i in range(1,N):
    if words[i][0]!=words[i-1][-1]:
        print("Player " + str(i%2+1) + " lost") #player 1 or player 2
        exit()

print("Fair Game")
