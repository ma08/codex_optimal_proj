
N = int(input())

if N < 2:
    print('No')
    exit()

word_list = []
for i in range(N):
    word = input()
    if len(word_list) == 0:
        word_list.append(word)
        continue
    if word_list[-1][-1] != word[0]:
        print('No')
        exit()
    if word in word_list:
        print('No')
        exit()
    word_list.append(word)
print('Yes')