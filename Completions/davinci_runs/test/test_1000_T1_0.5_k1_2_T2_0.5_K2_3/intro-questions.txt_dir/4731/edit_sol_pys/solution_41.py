

N = int(input())
words = []
for i in range(N):
    words.append(input())

if words[0][0] == words[1][0]:
    for i in range(1, N - 1):
        if words[i][-1] == words[i + 1][-1]:
            continue
        else:
            print("Player", i + 1, "lost")
            break
    else: 
        print("Fair Game")
else:
    print("Player", words.index(max(set(words), key=words.count)) + 1, "lost") 
