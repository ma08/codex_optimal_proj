

N = int(input())
S = input()

count = 0

for i in range(N-2):
    if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C': #文字列を１文字ずつ取り出す
        count += 1

print(count)
