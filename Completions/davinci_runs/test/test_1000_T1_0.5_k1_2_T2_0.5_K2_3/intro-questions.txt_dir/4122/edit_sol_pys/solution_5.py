# Problem

'''
You are given a positive integer H and a non-empty array of positive integers d.

Your goal is to find the minimum number of minutes needed to bring H down to 0.

Each minute, you can reduce H by any non-negative integer amount (including 0)
by using any of the integers in the array d.

For example, if H=20 and d=[3,5], it takes 2 minutes to bring H down to 0.

The first minute, you can reduce it by 3.

The second minute, you can reduce it by 5.

Write a function:

def solution(H, d)

that, given a positive integer H and a non-empty array of positive integers d,
returns the minimum number of minutes needed to bring H down to 0.

If it's impossible to bring H down to 0, the function should return -1.

For example, given H=20 and d=[3,5], the function should return 2,
as explained above.

Given H=20 and d=[1,10,2], the function should return 3.

The first minute, you can reduce H by 1.

The second minute, you can reduce it by 10.

The third minute, you can reduce it by 2.

Given H=10 and d=[1,2,3,4,5,6,7,8,9,10], the function should return 5.

The first minute, you can reduce H by 1.

The second minute, you can reduce it by 2.

The third minute, you can reduce it by 3.

The fourth minute, you can reduce it by 4.

The fifth minute, you can reduce it by 5.

Given H=1 and d=[1,1,1,1,1,1,1,1,1,1], the function should return -1.

It's impossible to reduce H in any number of minutes.

Given H=1 and d=[1], the function should return 1.

Given H=1 and d=[2], the function should return -1.

Given H=4 and d=[3,4], the function should return 2.

The first minute, you can reduce H by 3.

The second minute, you can reduce it by 4.

Given H=4 and d=[3,5], the function should return 3.

The first minute, you can reduce H by 3.

The second minute, you can reduce it by 3.

The third minute, you can reduce it by 3.

Given H=4 and d=[3,3,3], the function should return -1.

Given H=10 and d=[3,4,5], the function should return 3.

The first minute, you can reduce H by 3.

The second minute, you can reduce it by 4.

The third minute, you can reduce it by 3.

Given H=10 and d=[3,3,3], the function should return -1.

Given H=100 and d=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1

# Solution

H, n = map(int, input().split())
d = list(map(int, input().split()))

hp = H
minute = 0

for i in range(n):
    hp += d[i]
    minute += 1
    if hp <= 0:
        print(minute)
        break
else:
    print(-1)
