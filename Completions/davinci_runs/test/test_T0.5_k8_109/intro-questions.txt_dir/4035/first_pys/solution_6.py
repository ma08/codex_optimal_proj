

# Read input
A, B = map(int, input().split())

# Assume that the price is p yen and the consumption tax rate is r percent
# Then, the amount of consumption tax levied on it is:
#     \lfloor p \times \frac{r}{100} \rfloor
# Hence, we have:
#     p \times \frac{r}{100} - 1 < \lfloor p \times \frac{r}{100} \rfloor \leq p \times \frac{r}{100}
#     p \times \frac{r}{100} - 1 < A \leq B < p \times \frac{r}{100} + 1
#     p > \frac{A + B + 100}{r}
#     p > \frac{A + B + 100}{8}
#     p > \frac{A + B + 100}{10}
#     p > \frac{2 \times 2 + 100}{8} = \frac{104}{8} = 13
#     p > \frac{2 \times 2 + 100}{10} = \frac{104}{10} = 10
#     p > 13

# Initialize the price to be 13
p = 13

# Find the minimum price that satisfies the condition
while True:
    if p * 0.08 - 1 < A <= B < p * 0.1 + 1:
        break
    p += 1

# If there is no price that satisfies the condition, print -1
if p > 100:
    print(-1)
else:
    print(p)