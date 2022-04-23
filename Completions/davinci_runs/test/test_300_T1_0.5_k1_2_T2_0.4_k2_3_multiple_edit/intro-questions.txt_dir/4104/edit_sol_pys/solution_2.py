

def main():
    expression = input()
    result = 0
    for i in expression.split('+'):
        for j in i.split('-'): result += int(j)
        result -= len(i.split('-')) - 1 if '-' in i else 0
    print(result)

main()
