import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())

if N < 2:
    print('No')
    exit()

word_list = []
for i in range(N):
    word = readline().rstrip().decode()
    if len(word_list) == 0:
        word_list.append(word)
        continue
    if word_list[-1][-1] != word[0]:  # 最後の文字と最初の文字が一致しないとダメ
        print('No')
        exit()
    if word in word_list:  # 同じ単語が登場したらダメ
        print('No')
        exit()
    word_list.append(word)
print('Yes')
