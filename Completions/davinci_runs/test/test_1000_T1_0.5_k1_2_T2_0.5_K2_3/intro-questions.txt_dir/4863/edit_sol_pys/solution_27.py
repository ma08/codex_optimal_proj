

n = int(input())
s = 0
for i in range(1, n+1):
    answer = input().strip()
    if answer == 'A' or answer == 'a' or answer == 'E' or answer == 'e' or answer == 'I' or answer == 'i' or answer == 'O' or answer == 'o' or answer == 'U' or answer == 'u':
        s += 1
print(s)
