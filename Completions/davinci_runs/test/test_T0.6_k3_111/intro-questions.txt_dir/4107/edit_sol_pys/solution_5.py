
n, k = map(int, input().split())
s = input()

# if the room has a router, place one
# if the room does not have a router, connect directly

# we start with the room 1
# let's say the previous router was placed in room i
# let's say we want to connect room j
# if j-i > 2*k+1, we place a router in room i+k+1 and connect i+k+1 to j
# if j-i <= 2*k+1, we connect j

ans = 0
i = 1
for j in range(1, n+1):
    if j-i > 2*k+1:
        ans += i+k+1
        i = i+k+1
    if s[j-1] == "1":
        ans += j
        i = j

print(ans)
