
a = []
for i in range(0,N):
    a.append(int(input()))
print(a)
N = int(input())

# Alice wins if N is odd, otherwise Bob wins
if N % 2 == 0:
    print("Bob",end="")
else:
    print("Alice",end="")
