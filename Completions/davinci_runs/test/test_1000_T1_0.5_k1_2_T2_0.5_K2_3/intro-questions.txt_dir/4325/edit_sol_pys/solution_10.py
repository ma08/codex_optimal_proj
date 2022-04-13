
# 何個入っているか、何個入れられるか、何分かかるか
n = int(input())
x = int(input())
t = int(input())

if n % x == 0:
    print(t * (n // x))
else:
    print(t * (n // x + 1))
