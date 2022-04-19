# My answer
n = int(input())
s = input()


if s == 'ABC':
    print('ARC')
else:
    print('ABC')

# Reference answer
n = int(input())
s = input()

likes = []
for i in range(n):
    likes.append(list(map(int, input().split()))[1:])

foods = []
for i in range(m):
    foods.append(i+1)

for i in range(n):
    foods = list(set(foods) & set(likes[i]))

print(len(foods))
