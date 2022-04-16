

# Solution1

n = int(input())
s = input()

t = ""

# If the first two lamps are the same color, change the color of the first
# lamp.
if s[0] == s[1]:
    t += "R" if s[0] == "G" else "G"
else:
    t += s[0]

# If the last two lamps are the same color, change the color of the last
# lamp.
if s[n - 1] == s[n - 2]:
    t += "R" if s[n - 1] == "G" else "G"
else:
    t += s[n - 1]

# Iterate through the lamps, excluding the first and last lamps.
for i in range(1, n - 1):
    # If the lamp is the same color as the previous and next lamps, change
    # the lamp to the remaining color.
    if s[i] == s[i - 1] and s[i] == s[i + 1]:
        t += "R" if s[i] != "R" else "G"
    # If the lamp is the same color as the previous or next lamps, change
    # the lamp to the remaining color.
    elif s[i] == s[i - 1] or s[i] == s[i + 1]:
        t += "R" if s[i] != "R" else "G"
    # If the lamp is not the same color as the previous or next lamps,
    # change the lamp to the remaining color.
    else:
        t += "R" if s[i] != "R" else "G"

# Count the number of lamps that were changed.
num_changes = sum(1 for i in range(n) if t[i] != s[i])

# Print the number of lamps that were changed.
print(num_changes)

# Print the new garland.
print(t)




# Solution2

n = int(input())
s = input()

# If the first two lamps are the same color, change the color of the first
# lamp.
if s[0] == s[1]:
    s = "R" + s[1:] if s[0] == "G" else "G" + s[1:]

# If the last two lamps are the same color, change the color of the last
# lamp.
if s[n - 1] == s[n - 2]:
    s = s[:n - 1] + ("R" if s[n - 1] == "G" else "G")

# Iterate through the lamps, excluding the first and last lamps.
for i in range(1, n - 1):
    # If the lamp is the same color as the previous and next lamps, change
    # the lamp to the remaining color.
    if s[i] == s[i - 1] and s[i] == s[i + 1]:
        s = s[:i] + ("R" if s[i] != "R" else "G") + s[i + 1:]
    # If the lamp is the same color as the previous or next lamps, change
    # the lamp to the remaining color.
    elif s[i] == s[i - 1] or s[i] == s[i + 1]:
        s = s[:i] + ("R" if s[i] != "R" else "G") + s[i + 1:]
    # If the lamp is not the same color as the previous or next lamps,
    # change the lamp to the remaining color.
    else:
        s = s[:i] + ("R" if s[i] != "R" else "G") + s[i + 1:]

# Count the number of lamps that were changed.
num_changes = sum(1 for i in range(n) if t[i] != s[i])

# Print the number of lamps that were changed.
print(num_changes)

# Print the new garland.
print(s)
