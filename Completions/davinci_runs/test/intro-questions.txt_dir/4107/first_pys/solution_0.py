

n, k = map(int, input().split())
s = input()

# if the room has a router, place one
# if the room does not have a router, connect directly
# if the room has a router and it is too close to the previous router, connect directly
# if the room has a router and it is too far from the previous router, connect directly and place a router
# if the room does not have a router and it is too close to the previous router, connect directly
# if the room does not have a router and it is too far from the previous router, connect directly

# we start with the room 1
# let's say the previous router was placed in room i
# let's say we want to connect room j
# if j-i > 2*k+1, we place a router in room i+k+1 and connect i+k+1
# if j-i <= 2*k+1, we connect j
# if j-i <= k, we connect j
# if j-i > k, we connect j
# if j-i <= 2*k, we connect j
# if j-i > 2*k, we place a router in j-k and connect j-k
# if j-i <= 3*k, we connect j
# if j-i > 3*k, we connect j

# if the room has a router, place one
# if the room does not have a router, connect directly

# we start with the room 1
# let's say the previous router was placed in room i
# let's say we want to connect room j
# if j-i > 2*k+1, we place a router in room i+k+1 and connect i+k+1
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