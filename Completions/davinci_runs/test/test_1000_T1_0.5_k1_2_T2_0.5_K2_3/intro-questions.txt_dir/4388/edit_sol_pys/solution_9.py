

import sys

n = int(input())

if (111 <= n <= 999):
    n = str(n)
    n = n.replace("1", "*")  # Заменяем 1 на *
    n = n.replace("9", "1")  # Заменяем 9 на 1
    n = n.replace("*", "9")  # Заменяем * на 9
    print (n)
else:
    sys.exit()
