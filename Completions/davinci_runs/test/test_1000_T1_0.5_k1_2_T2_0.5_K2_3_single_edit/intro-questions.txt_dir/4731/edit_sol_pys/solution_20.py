n = int(input())
words = [input() for i in range(n)]


if words[0][-1] != words[1][0]:
    print("Player 1 lost")
elif n > 1 and words[1] == words[2]:
    print("Player 1 lost")
else:
    print("Fair Game")    
