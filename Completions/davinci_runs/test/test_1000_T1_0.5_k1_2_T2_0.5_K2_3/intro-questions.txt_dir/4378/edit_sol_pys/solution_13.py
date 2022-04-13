
# Solution

n = int(input())
s = input()

t = ""

# If the first two bulbs are the same color, change the color of the first lamp.
if s[0] == s[1]:
    t += "R" if s[0] == "G" else "G"
else:
    t += s[0]

# If the last two bulbs are the same color, change the color of the last lamp.
if s[n - 1] == s[n - 2]:
    t += "R" if s[n - 1] == "G" else "G"
else:
    t += s[n - 1]

# Iterate through the bulbs, excluding the first and last bulbs.
for i in range(1, n - 1):
    # If the bulb is the same color as the previous and next bulbs, change the bulb to the remaining color.
    if s[i] == s[i - 1] and s[i] == s[i + 1]:
        t += "R" if s[i] != "R" else "G"
    # If the bulb is the same color as the previous or next bulbs, change the bulb to the remaining color.
    elif s[i] == s[i - 1] or s[i] == s[i + 1]:
        t += "R" if s[i] != "R" else "G"
    # If the bulb is not the same color as the previous or next bulbs,
    # change the bulb to the remaining color.
    else:
        t += "R" if s[i] != "R" else "G"

# Count the number of lamps that were changed.
num_changes = sum(1 for i in range(n) if t[i] != s[i])

# Print the number of lamps that were changed.
print(num_changes)

# Print the new garland.
print(t)
