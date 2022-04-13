
n = int(input())  # 3
t = input()  # aab

s = [t[0]]

for i in range(1, n):
    if t[i] != t[i-1]:
        s.append(t[i])
print(''.join(s))
