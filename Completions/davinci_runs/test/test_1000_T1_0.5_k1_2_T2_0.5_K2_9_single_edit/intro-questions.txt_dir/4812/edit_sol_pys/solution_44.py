

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
    words = phrase.split()
    for word in words:
        for ending in endings:
            if word.endswith(tuple(ending)):
                if words[-1] == word:
                    print("YES")
                else:
                    print("NO")
