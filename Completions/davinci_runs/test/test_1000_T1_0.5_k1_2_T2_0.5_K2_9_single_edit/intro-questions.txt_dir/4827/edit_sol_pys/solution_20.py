

n = int(input())
words = []
for i in range(n):
    words.append(input())

num = len(''.join(words[:words.index('$')])) + len(''.join(words[words.index('$')+1:]))

if num < 11:
    print(' '.join(words[:words.index('$')]), str(num), ' '.join(words[words.index('$')+1:]))
elif num < 20:
    print(' '.join(words[:words.index('$')]), str(num+10), ' '.join(words[words.index('$')+1:]))
elif num < 100:
    print(' '.join(words[:words.index('$')]), str(num//10), str(num%10), ' '.join(words[words.index('$')+1:]))
elif num < 1000:
    print(' '.join(words[:words.index('$')]), str(num//100), str(num%100//10), str(num%100%10), ' '.join(words[words.index('$')+1:]))
