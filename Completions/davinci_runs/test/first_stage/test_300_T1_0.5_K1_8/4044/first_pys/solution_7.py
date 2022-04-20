

from random import shuffle

def create_binary_string(a, b, x):
    string = [0] * a + [1] * b
    shuffle(string)
    string = list(map(str, string))
    return ''.join(string)

def check_binary_string(string):
    count = 0
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            count += 1
    return count

if __name__ == "__main__":
    a, b, x = map(int, input().split())
    string = create_binary_string(a, b, x)
    while check_binary_string(string) != x:
        string = create_binary_string(a, b, x)
    print(string)