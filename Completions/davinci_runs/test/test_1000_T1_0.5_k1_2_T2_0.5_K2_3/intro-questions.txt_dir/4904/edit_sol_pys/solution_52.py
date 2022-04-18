import re

def main():
    game_record = re.findall(r'[AB]\d', input())
    alice_score = 0
    barbara_score = 0
    for i in range(len(game_record)):
        if game_record[i][0] == 'A':
            alice_score += int(game_record[i][1])
        else:
            barbara_score += int(game_record[i][1])
        if (alice_score >= 11 or barbara_score >= 11) and abs(alice_score - barbara_score) >= 2:
            break
    if alice_score > barbara_score:
        print('A')
    else:
        print('B')

if __name__ == '__main__':
    main()
