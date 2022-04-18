
n = int(input())
s = input()

counter = 1
max_counter = 1

for i in range(1, n):
    if s[i] == s[i - 1]:
        counter += 1
    else:
        max_counter = max(max_counter, counter)
        counter = 1

print(max(max_counter, counter))
