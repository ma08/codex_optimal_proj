
x = input()
if x[0] in 'aeiouAEIOU':
    print(x + 'way')
elif x[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
    print(x[1:] + x[0] + 'ay')
