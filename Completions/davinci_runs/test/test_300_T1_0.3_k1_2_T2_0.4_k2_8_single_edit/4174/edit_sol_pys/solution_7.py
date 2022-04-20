

n, x = map(int, input().split())
l = list(map(int, input().split()))

# 初期値
count = 1
d = 0

for i in range(n):
    d += l[i]
    if d <= x:
        count += 1



# a = [1, 2, 3, 4, 5]
# print(a[:2])
# print(a[2:])

# s = "stressed"
# print(s[::-1])

# a = "パタトクカシーー"
# print(a[::2])

# a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.".replace(",", "").replace(".", "")
# print(a)
# b = a.split()
# print(b)
# c = [len(i) for i in b]
# print(c)

# a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".replace(",", "").replace(".", "")
# b = a.split()
# c = [1, 5, 6, 7, 8, 9, 15, 16, 19]
# d = {}
# for i, v in enumerate(b, 1):
#     if i in c:
#         d[v[:1]] = i
#     else:
#         d[v[:2]] = i
# print(d)

# a = "paraparaparadise"
# b = "paragraph"
# X = set(a)
# Y = set(b)
# print(X | Y)
# print(X & Y)
# print(X - Y)
# print(Y - X)
# print("se" in X)
# print("se" in Y)

# def n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# a = "I am an NLPer"
# print(n_gram(a, 2))
# b = a.split()
# print(n_gram(b, 2))

# def char_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# def word_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# a = "I am an NLPer"
# print(char_n_gram(a, 2))
# b = a.split()
# print(word_n_gram(b, 2))

# def char_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# def word_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# a = "I am an NLPer"
# print(char_n_gram(a, 2))
# b = a.split()
# print(word_n_gram(b, 2))

# def char_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# def word_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# a = "I am an NLPer"
# print(char_n_gram(a, 2))
# b = a.split()
# print(word_n_gram(b, 2))

# def char_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# def word_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# a = "I am an NLPer"
# print(char_n_gram(a, 2))
# b = a.split()
# print(word_n_gram(b, 2))

# def char_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# def word_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# a = "I am an NLPer"
# print(char_n_gram(a, 2))
# b = a.split()
# print(word_n_gram(b, 2))

# def char_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# def word_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# a = "I am an NLPer"
# print(char_n_gram(a, 2))
# b = a.split()
# print(word_n_gram(b, 2))

# def char_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# def word_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# a = "I am an NLPer"
# print(char_n_gram(a, 2))
# b = a.split()
# print(word_n_gram(b, 2))

# def char_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# def word_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# a = "I am an NLPer"
# print(char_n_gram(a, 2))
# b = a.split()
# print(word_n_gram(b, 2))

# def char_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# def word_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# a = "I am an NLPer"
# print(char_n_gram(a, 2))
# b = a.split()
# print(word_n_gram(b, 2))

# def char_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# def word_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# a = "I am an NLPer"
# print(char_n_gram(a, 2))
# b = a.split()
# print(word_n_gram(b, 2))

# def char_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# def word_n_gram(target, n):
#     return [target[i:i+n] for i in range(len(target)-n+1)]

# a = "I am an NLPer"
# print(char_n_gram(a, 2))
# b = a.split()
# print(word_n_gram(b, 2))
print(count)
