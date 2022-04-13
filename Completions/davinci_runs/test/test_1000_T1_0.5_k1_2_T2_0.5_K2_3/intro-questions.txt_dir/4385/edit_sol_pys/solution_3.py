
# 解説を参考に作成
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

if abs(b - a) > k:
    print(':(')
elif abs(c - b) > k:
    print(':(')
elif abs(d - c) > k:
    print(':(')
elif abs(e - d) > k:
    print(':(')
else:
    print('Yay!')
