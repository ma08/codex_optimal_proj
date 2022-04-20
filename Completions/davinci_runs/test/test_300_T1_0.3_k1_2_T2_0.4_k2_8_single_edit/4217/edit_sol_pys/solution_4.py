

# My answer
n, m = map(int, input().split())
likes = []
for i in range(n):
    likes.append(list(map(int, input().split()))[1:])
foods = []
for i in range(m):
    foods.append(i+1)
for i in range(n):
    foods = list(set(foods) & set(likes[i]))
print(len(foods))

# Reference answer
n, m = map(int, input().split())
likes = []
for i in range(n):
    likes.append(list(map(int, input().split()))[1:])
foods = []
for i in range(m):
    foods.append(i+1)
for i in range(n):
    foods = list(set(foods) & set(likes[i]))
print(len(foods))
