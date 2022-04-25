
N = int(input())

words = [input()]
for i in range(N):
    word = input()
    if word not in words or word[0] != words[-1][-1]:
        print("No")
        exit()
    words.append(word)

print("Yes") 
