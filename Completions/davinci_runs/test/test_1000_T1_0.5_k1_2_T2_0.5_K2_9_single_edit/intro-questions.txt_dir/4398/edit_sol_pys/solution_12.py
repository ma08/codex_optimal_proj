

N = int(input())
S,T = input().split()

string = ""
for i in range(N):
    string += S[i]
    string += T[i]

print(string)
