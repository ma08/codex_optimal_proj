

def main():
    expression = input().split('+')
    result = 0
    for i in expression:
        for j in i.split('-'):
            result += int(j)
        result -= len(i.split('-')) - 1
    print(result)
