
S = input()
E = int(input())
endings = []
for _ in range(E):
    endings.append(set(input().split()))
P = int(input())
phrases = []
for _ in range(P):
    phrases.append(input())

for phrase in phrases:
    if phrase.endswith(tuple(endings)):
        print("YES")
    else:
        print("NO")
