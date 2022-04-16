

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
    for i in endings:
        if word in i:
            return i
    return False

for phrase in phrases:
    if len(phrase) == 2:
        if check(phrase[1]):
            if check(phrase[1]) == check(S[-len(phrase[1]):]) and len(check(phrase[1])) != 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        if check(phrase[1]) and check(phrase[2]):
            if check(phrase[1]) == check(phrase[2]) and check(phrase[2]) == check(S[-len(phrase[2]):]) and len(check(phrase[1])) != 0 and len(check(phrase[2])) != 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
