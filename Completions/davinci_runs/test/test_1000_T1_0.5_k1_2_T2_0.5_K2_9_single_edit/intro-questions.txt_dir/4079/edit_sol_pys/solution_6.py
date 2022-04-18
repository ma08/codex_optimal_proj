

n = int(input())
lst = []
for i in range(n):
    lst.append(input())

for i in lst: # строка
    if len(i) == len(set(i)) and len(set(i)) == ord(max(i)) - ord(min(i)) + 1: # длина строки равна длине множества символов строки и длине множества символов строки равна разности максимального и минимального символа плюс единица
        print("Yes")
    else:
        print("No")
