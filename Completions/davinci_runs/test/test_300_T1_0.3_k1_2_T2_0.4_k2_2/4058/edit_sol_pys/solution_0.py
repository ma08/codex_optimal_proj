#-----Solution-----

n, r = map(int, input().split())
a = list(map(int, input().split()))

# The answer is the number of unwarmed elements
# plus the number of heaters that are not warming up
# any unwarmed elements

unwarmed = 0
heaters = 0

for i in range(n):
    if a[i] == 0:
        unwarmed += 1
    else:
        # If the heater is not warming up any unwarmed elements,
        # it is not needed
        if i - r + 1 <= 0 or a[i - r] == 0:
            heaters += 1

if unwarmed == 0:
    print(heaters)
else:
    print(-1)
