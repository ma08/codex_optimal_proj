
# 解説を参考に作成
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

if (a - b) > k:
    print(':(')
elif (b - c) > k:
    print(':(')
elif (c - d) > k:
    print(':(')
elif (d - e) > k:
    print(':(')
else:
    print('Yay!')
