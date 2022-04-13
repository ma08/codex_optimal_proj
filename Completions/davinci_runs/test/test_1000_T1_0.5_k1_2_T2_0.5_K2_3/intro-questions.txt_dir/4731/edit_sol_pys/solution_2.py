
N = int(input())
words = []
for i in range(N):
    words.append(input())

if len(words) == len(set(words)):
    if words[0][0] == words[1][-1]:
        for i in range(1, N - 1):
            if words[i][-1] == words[i + 1][0]:
                continue
            else:
                print("Player", i + 1, "loses")
                break
        else:
            print("Fair Game")
    else:
        print("Player 1 loses")
else:
    print("Player", words.index(max(set(words), key=words.count)) + 1, "loses")
