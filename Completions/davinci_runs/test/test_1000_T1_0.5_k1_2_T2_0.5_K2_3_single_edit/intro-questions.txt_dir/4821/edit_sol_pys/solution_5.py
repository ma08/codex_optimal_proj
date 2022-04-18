

def razlika(brojevi):
    for suit in brojevi:
        if brojevi[suit] != 13:
            print(13 - brojevi[suit], end=' ')
    print()

def main():
    brojevi = {'P': 0, 'K': 0, 'H': 0, 'T': 0}
    for i in input():
        brojevi[i[0]] += 1
    razlika(brojevi)

main()
