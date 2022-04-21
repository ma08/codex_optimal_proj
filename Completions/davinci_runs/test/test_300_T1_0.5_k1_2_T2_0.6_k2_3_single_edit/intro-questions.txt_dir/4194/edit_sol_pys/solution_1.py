# coding:utf-8
# 文字列を扱う
s = 'Hello World!'
s = s.replace('World','Python')
print(s)

# 数値を扱う
a = 1
b = 2
c = a + b
print(c)

# 配列を扱う
sample_list = [1,2,3,4,5]
print(sample_list)

# リスト生成
sample_list = range(1,10)
print(sample_list)

# リストの要素を足し合わせる
sample_list = range(1,10)
sum = 0
for i in sample_list:
    sum += i
print(sum)

# リストの要素を足し合わせる
sample_list = range(1,10)
sum = 0
for i in sample_list:
    if i % 2 == 1:
        sum += i
print(sum)

# if文
a = 5
if a < 5:
    print('aは5より小さい')
elif a > 5:
    print('aは5より大きい')
else:
    print('aは5と等しい')

# 関数
def func1():
    print('func1')
func1()
