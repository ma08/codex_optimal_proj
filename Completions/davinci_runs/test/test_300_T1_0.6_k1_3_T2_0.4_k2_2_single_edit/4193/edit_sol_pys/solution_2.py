
import sys

def read_input(path):
    if not path:
        path = './input.txt'
    with open(path) as f:
        lines = [line.rstrip() for line in f]
    return lines

def process_input(lines):
    card = []
    for i in range(3):
        card.append([int(x) for x in lines[i].split(' ')])
    bs = [int(x) for x in lines[4:]]
    return card, bs

def is_bingo(card, bs):
    for i in range(3):
        for j in range(3):
            for b in bs:
                if b == card[i][j]:
                    card[i][j] = -1
    for i in range(3):
        if card[i][0] == -1 and card[i][1] == -1 and card[i][2] == -1:
            return True
    for j in range(3):
        if card[0][j] == -1 and card[1][j] == -1 and card[2][j] == -1:
            return True
    if card[0][0] == -1 and card[1][1] == -1 and card[2][2] == -1:
        return True
    if card[2][0] == -1 and card[1][1] == -1 and card[0][2] == -1:
        return True
    return False

def write_output(path, output):
    if not path:
        path = './output.txt'
    with open(path, mode='w') as f:
        f.write(output)

def main(path=''):
    lines = read_input(path)
    card, bs = process_input(lines)
    output = 'Yes' if is_bingo(card, bs) else 'No'
    write_output(path, output)

if __name__ == "__main__":
    main(sys.argv[1])
