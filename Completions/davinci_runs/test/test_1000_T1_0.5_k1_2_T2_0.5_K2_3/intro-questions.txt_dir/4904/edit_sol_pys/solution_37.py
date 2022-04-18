

def main():
    # parse input
    games = raw_input()
    alices = 0
    barbaras = 0

    for i in range(0, len(games), 2):
        if games[i] == 'A':
            if games[i + 1] == '1':
                alices += 1
            else:
                alices += 2
        else:
            if games[i + 1] == '1':
                barbaras += 1
            else:
                barbaras += 2

    # determine the winner
    if alices == 11 and barbaras == 10:
        print('A')
    elif barbaras == 11 and alices == 10:
        print('B')
    elif alices > barbaras:
        print('A')
    elif barbaras > alices:
        print('B')
    else:
        print('error')

if __name__ == '__main__':
    main()
