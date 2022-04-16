

num = input()
num = num[::-1]
num = num + (3 - len(num) % 3) * '0'
oct = ''
for i in range(0, len(num), 3):
    oct += str(int(num[i:i + 3], 2))

print(int(oct[::-1]))
