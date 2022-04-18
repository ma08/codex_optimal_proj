
def main(file):
    with open(file) as f:
        words = []
        for line in f:
            line = line.strip().split()
            for word in line:
                if word.lower() not in words:
                    words.append(word.lower())
                    print(word, end=' ')
                else:
                    print('.', end=' ')
            print('')
if __name__ == '__main__':
    main(sys.argv[1])
