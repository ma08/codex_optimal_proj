

def main():
    expression = input().split(' ')
    result = 0
    for i in expression:
        result += int(i)
    print(result)


main()
