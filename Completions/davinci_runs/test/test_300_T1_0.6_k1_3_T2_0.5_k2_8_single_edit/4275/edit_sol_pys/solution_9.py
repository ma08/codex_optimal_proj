

# S = input()
# if S[2] == S[3] and S[4] == S[5]:
#     print("Yes")
# else:
#     print("No")


# print(list(range(1, 100)))
# print(list(range(100)))

# print(list(range(1, 100, 2)))

# print(list(range(5, 0, -1)))

# print(list(range(5, 0)))

# print(list(range(0, 5, -1)))

# print(list(range(0, 5)))

# print(list(range(0, 5, -1)))


# for i in range(5):
#     print(i)

# for i in range(1, 5):
#     print(i)

# for i in range(1, 5, 2):
#     print(i)

# for i in range(5, 0, -1):
#     print(i)

# for i in range(0, 5, -1):
#     print(i)

# for i in range(0, 5):
#     print(i)

# for i in range(0, 5, -1):
#     print(i)


# S = "stressed"
# print(S[::-1])

# S = "パタトクカシーー"
# print(S[::2])

# S = "パトカー"
# T = "タクシー"
# print("".join([s+t for s, t in zip(S, T)]))

# S = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# print(list(map(len, S.split())))


# def cipher(S):
#     return "".join([chr(219 - ord(c)) if c.islower() else c for c in S])


# S = "I am an NLPer"
# print(cipher(S))

# print(cipher(cipher(S)))


# def ngram(S, n):
#     return [S[i:i+n] for i in range(len(S)-n+1)]

# S = "I am an NLPer"
# print(ngram(S, 2))
# print(ngram(S.split(), 2))

# S = "paraparaparadise"
# T = "paragraph"
# X = set(ngram(S, 2))
# Y = set(ngram(T, 2))
# print("X:", X)
# print("Y:", Y)
# print("X|Y:", X|Y)
# print("X&Y:", X&Y)
# print("X-Y:", X-Y)
# print("'se' in X:", 'se' in X)
# print("'se' in Y:", 'se' in Y)


# def is_word(word):
#     return word.isalpha()

# def is_sentence(sentence):
#     return sentence.isalpha()

# def is_sentence(sentence):
#     for word in sentence.split():
#         if not word.isalpha():
#             return False
#     return True

# def is_sentence(sentence):
#     return all(map(str.isalpha, sentence.split()))

# def is_sentence(sentence):
#     return all(word.isalpha() for word in sentence.split())


# def is_sentence(sentence):
#     return all(map(str.isalpha, sentence.split()))

# print(is_sentence("I am a boy."))
# print(is_sentence("I am a boy."))


# def is_word(word):
#     return word.isalpha()

# def is_sentence(sentence):
#     return all(map(str.isalpha, sentence.split()))

# def is_sentence(sentence):
#     return all(word.isalpha() for word in sentence.split())


# def is_word(word):
#     return word.isalpha()

# def is_sentence(sentence):
#     return all(map(str.isalpha, sentence.split()))

# def is_sentence(sentence):
#     return all(word.isalpha() for word in sentence.split())


# def is_word(word):
#     return word.isalpha()

# def is_sentence(sentence):
#     return all(map(str.isalpha, sentence.split()))

# def is_sentence(sentence):
#     return all(word.isalpha() for word in sentence.split())


# def is_word(word):
#     return word.isalpha()

# def is_sentence(sentence):
#     return all(map(str.isalpha, sentence.split()))

# def is_sentence(sentence):
#     return all(word.isalpha() for word in sentence.split())


# def is_word(word):
#     return word.isalpha()

# def is_sentence(sentence):
#     return all(map(str.isalpha, sentence.split()))

# def is_sentence(sentence):
#     return all(word.isalpha() for word in sentence.split())


# def is_word(word):
#     return word.isalpha()

# def is_sentence(sentence):
#     return all(map(str.isalpha, sentence.split()))

# def is_sentence(sentence):
#     return all(word.isalpha() for word in sentence.split())


# def is_word(word):
#     return word.isalpha()

# def is_sentence(sentence):
#     return all(map(str.isalpha, sentence.split()))

# def is_sentence(sentence):
#     return all(word.isalpha() for word in sentence.split())


# def is_word(word):
#     return word.isalpha()

# def is_sentence(sentence):
#     return all(map(str.isalpha, sentence.split()))

# def is_sentence(sentence):
#     return all(word.isalpha() for word in sentence.split())


# def is_word(word):
#     return word.isalpha()

# def is_sentence(sentence):
#     return all(map(str.isalpha, sentence.split()))

# def is_sentence(sentence):
#     return all(word.isalpha() for word in sentence.split())


# def is_word(word):
#     return word.isalpha()

# def is_sentence(sentence):
#     return all(map(str.isalpha, sentence.split()))

# def is_sentence(sentence):
#     return all(word.isalpha() for word in sentence.split())


# def is_word(word):
#     return word.isalpha()

# def is_sentence(sentence):
#     return all(map(str.isalpha, sentence.split()))

