

# My solution.

sentence = input()
words = sentence.split()

words_with_ae = 0

for word in words:
    if 'ae' in word:
        words_with_ae += 1

if words_with_ae / len(words) >= 0.4:
    print('dae ae ju traeligt va') # dä ä ju tråligt va
else:
    print('haer talar vi rikssvenska') # här talar vi rikssvenska
