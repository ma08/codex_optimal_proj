

def main():
    expression = input().split('-')
    result = 0
    for i in expression:
        i = i.split('+')
        for j in i:
            result += int(j)
        result -= 1
    print(result)

main()
