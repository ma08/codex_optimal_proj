

sentence = input()
words = sentence.split()  # My solution

words_with_ae = 0

for word in words:
    if 'ae' in word:
        words_with_ae += 1

if words_with_ae / len(words) >= 0.4:
    print('dae ae ju traeligt va')  # Swedish for "you are very tired"
else:
    print('haer talar vi rikssvenska')  # Swedish for "here we speak Swedish"
