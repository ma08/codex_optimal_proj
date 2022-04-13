

S = input()
E = int(input())
endings = []
for i in range(E):
    endings.append(input().split())
P = int(input())
phrases = []
for i in range(P):
    phrases.append(input().split())

def check(word):
    for i in range(len(endings)):
        if word == endings[i][0]:
            return endings[i]
    return False

for phrase in phrases:
    if len(phrase) == 2:
        if check(phrase[1]) and check(S[-len(phrase[1]):]): # check if the word is in the endings and if the ending of the sentence is in the endings
            if check(phrase[1]) == check(S[-len(phrase[1]):]): # check if the word in the phrase and the ending of the sentence have the same ending
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        if check(phrase[1]) and check(phrase[3]) and check(S[-len(phrase[3]):]):
            if check(phrase[1]) == check(phrase[3]) and check(phrase[3]) == check(S[-len(phrase[3]):]):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
