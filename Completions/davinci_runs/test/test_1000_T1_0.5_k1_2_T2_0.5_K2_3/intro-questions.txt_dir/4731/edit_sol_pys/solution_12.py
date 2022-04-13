
N = int(input())
words = list()
for i in range(N):
    words.append(input().lower())

if len(words) == len(set(words)):
    for i in range(N - 1):
        if words[i][-1] == words[i + 1][0]:
            continue
        else:
            print("Player", i + 1, "lost.")
            break
    else: 
        print("Fair Game.")
else:
    print("Player", words.index(max(set(words), key=words.count)) + 1, "lost.")
