

S = input()
E = int(input())
endings = []
for i in range(E):
    endings.append(input())
P = int(input())
phrases = []
for i in range(P):
    phrases.append(input())

def check(word):
    for i in endings:
        if word[-len(i):] == i:
            return i
    return False

for phrase in phrases:
    if len(phrase) == 2:
        if check(phrase[1]) and check(S):
            if check(phrase[1]) == check(S):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        if check(phrase[1]) and check(phrase[2]) and check(S):
            if check(phrase[1]) == check(phrase[2]) and check(phrase[2]) == check(S):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
