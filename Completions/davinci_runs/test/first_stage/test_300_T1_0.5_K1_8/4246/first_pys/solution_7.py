

# Read input
forecast = input()
actual = input()

# Count days where forecast == actual
correct = 0
for i in range(3):
    if forecast[i] == actual[i]:
        correct += 1

# Print count
print(correct)