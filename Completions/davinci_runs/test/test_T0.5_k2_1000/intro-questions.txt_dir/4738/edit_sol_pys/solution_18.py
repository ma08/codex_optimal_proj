

import os

def get_k(string):
    for k in range(1, len(string) + 1):
        if len(string) % k == 0:
            for i in range(k, len(string), k):
                if string[i:i+k] != string[i-k:i][-1] + string[i-k:i][:-1]: # проверяем соответствие подстроки предыдущей
                    break # если встретили несоответствие, проверяем следующее k
            else: # если не встретили несоответствий, возвращаем k
                return k 
    return len(string)

def main():
    string = os.read(0, os.fstat(0).st_size).decode()
    print(get_k(string))

if __name__ == '__main__':
    main()
