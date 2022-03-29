

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    names.sort()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = ''
    for i in range(len(names)-1):
        for j in range(min(len(names[i]), len(names[i+1]))):
            if names[i][j] != names[i+1][j]:
                new_alphabet += names[i][j]
                break
    if len(new_alphabet) == 26:
        print(new_alphabet)
    else:
        print('Impossible')

if __name__ == '__main__':
    main()