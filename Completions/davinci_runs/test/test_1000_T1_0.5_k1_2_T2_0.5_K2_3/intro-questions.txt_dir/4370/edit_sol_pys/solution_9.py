def canTake(a, b):
    if a + b > 16:
        return False
    if a == b:
        return False
    return True


a, b = map(int, input().split())  # Получаем два числа и преобразуем их в целые
if canTake(a, b):
    print('Yay!')
else:
    print(':(')
