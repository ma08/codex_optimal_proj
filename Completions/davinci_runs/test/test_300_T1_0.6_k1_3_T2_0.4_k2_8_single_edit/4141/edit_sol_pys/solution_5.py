

N = int(input())
A = []
for i in range(N):
    A.append(int(input()))  # inputをint型に変換して、リストAに追加

for i in A:
    if i % 2 == 0 and (i % 3 != 0 and i % 5 != 0):  # 偶数で、かつ3でも5でも割り切れない場合
        print('DENIED')
        exit(0)
print('APPROVED')
