import re

def main():
    f = open('sample.txt', 'r')
    text = f.read()
    f.close()

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans = max(ans, gcd(a_list[i], a_list[j]))

print(ans)
