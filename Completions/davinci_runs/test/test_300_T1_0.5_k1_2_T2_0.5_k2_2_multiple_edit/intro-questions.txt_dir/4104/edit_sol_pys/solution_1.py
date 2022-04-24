

def main():
    expresion = input()
    expresion = expresion.split('+')
    result = 0
    for i in expresion:
        i = i.split('-')
        for j in i:
            result += int(j)
        result -= len(i) - 1
    print(result)

if __name__ == '__main__':
    main()
